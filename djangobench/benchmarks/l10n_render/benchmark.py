import os

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render_to_response
from django.template  import RequestContext
from django.test.client import Client

from djangobench.utils import run_benchmark


def make_request():
    environ = {
        'PATH_INFO': '/',
        'QUERY_STRING': '',
        'REQUEST_METHOD': 'GET',
        'SCRIPT_NAME': '',
        'SERVER_NAME': 'testserver',
        'SERVER_PORT': 80,
        'SERVER_PROTOCOL': 'HTTP/1.1',
        }
    return WSGIRequest(environ)


req_object = make_request()


def benchmark():
    render_to_response('list.html',
                       {'numbers': range(0, 200)},
                       context_instance=RequestContext(req_object))


run_benchmark(
    benchmark,
    syncdb = False,
    meta = {
        'description': 'Render a l10n intensive template.',
    }
)
