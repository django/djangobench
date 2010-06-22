from time import time

from django.test.client import Client
from django.conf import global_settings
from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.core.handlers.wsgi import WSGIHandler

from djangobench.utils import run_comparison_benchmark

class RequestFactory(Client):
    """
    Class that lets you create mock Request objects for use in testing.
    
    Usage:
    
    rf = RequestFactory()
    get_request = rf.get('/hello/')
    post_request = rf.post('/submit/', {'foo': 'bar'})
    
    This class re-uses the django.test.client.Client interface, docs here:
    http://www.djangoproject.com/documentation/testing/#the-test-client
    
    Once you have a request object you can pass it to any view function, 
    just as if that view had been hooked up using a URLconf.
    
    Author: Simon (http://djangosnippets.org/users/simon/)
    djangosnippet URL: (http://djangosnippets.org/snippets/963/)
    """
    def request(self, **request):
        """
        Similar to parent class, but returns the request object as soon as it
        has created it.
        """
        environ = {
            'HTTP_COOKIE': self.cookies,
            'PATH_INFO': '/',
            'QUERY_STRING': '',
            'REQUEST_METHOD': 'GET',
            'SCRIPT_NAME': '',
            'SERVER_NAME': 'testserver',
            'SERVER_PORT': 80,
            'SERVER_PROTOCOL': 'HTTP/1.1',
        }
        environ.update(self.defaults)
        environ.update(request)

        return WSGIRequest(environ)

def setup():
    global req_factory, handler_default_middleware, handler_no_middleware
    req_factory = RequestFactory()
    
    settings.MIDDLEWARE_CLASSES = global_settings.MIDDLEWARE_CLASSES
    handler_default_middleware = WSGIHandler()
    handler_default_middleware.load_middleware()
    
    settings.MIDDLEWARE_CLASSES = []
    handler_no_middleware = WSGIHandler()
    handler_no_middleware.load_middleware()

def benchmark_request(middleware_classes):
    settings.MIDDLEWARE_CLASSES = middleware_classes
    req_factory = RequestFactory()
    handler = WSGIHandler()
    handler.load_middleware()
    handler.get_response(req_factory.get('/'))

def benchmark_default_middleware():
    global req_factory, handler_default_middleware
    handler_default_middleware.get_response(req_factory.get('/'))

def benchmark_no_middleware():
    global req_factory, handler_no_middleware
    handler_no_middleware.get_response(req_factory.get('/'))

run_comparison_benchmark(
    benchmark_default_middleware,
    benchmark_no_middleware, 
    setup = setup,
    syncdb = False,
    trials = 50
)