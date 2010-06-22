from django.core.urlresolvers import reverse

from utils import run_benchmark

def benchmark():
    reverse('url_resolve.views.basic')
    reverse('url_resolve.views.catchall')
    reverse('url_resolve.views.vars',args=[1,])
    reverse('url_resolve.views.vars',kwargs={'var':1})

run_benchmark(benchmark, trials=20)
