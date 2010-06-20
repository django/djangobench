import time

from django.core.urlresolvers import reverse, resolve

from utils import run_benchmark

def benchmark():
    resolve('/basic/')
    reverse('urls.views.basic')

run_benchmark(benchmark)
