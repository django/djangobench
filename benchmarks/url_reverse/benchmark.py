from django.core.urlresolvers import reverse

from utils import run_benchmark

def benchmark():
    reverse('url_resolve.views.basic')
    reverse('url_resolve.views.catchall')

run_benchmark(benchmark)
