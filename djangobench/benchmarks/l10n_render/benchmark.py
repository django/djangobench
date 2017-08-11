import sys

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render_to_response
from django.template import RequestContext

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
        "wsgi.input": sys.stdin
    }

    return WSGIRequest(environ)


req_object = make_request()


def benchmark():
    context = RequestContext(req_object)
    context['numbers'] = range(0, 200)
    render_to_response('list.html', context)


run_benchmark(
    benchmark,
    migrate = False,
    meta = {
        'description': 'Render a l10n intensive template.',
    }
)
