from time import time

from utils import run_benchmark

from django.test.client import Client
from django.core.handlers.wsgi import WSGIRequest
from django.core.handlers.wsgi import WSGIHandler

from default_middleware.views import index

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

def benchmark():

    req_factory = RequestFactory()
    handler = WSGIHandler()
    handler.load_middleware()

    with_middleware_time = time()
    handler.get_response(req_factory.get('/'))
    with_middleware_time = time() - with_middleware_time

    no_middleware_time = time()
    index(req_factory.get('/'))
    no_middleware_time = time() - no_middleware_time

    return with_middleware_time - no_middleware_time

run_benchmark(benchmark, trials=50)
