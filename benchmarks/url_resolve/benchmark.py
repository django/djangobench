from django.core.urlresolvers import resolve

from utils import run_benchmark

def benchmark():
    resolve('/basic/')
    resolve('/fallthroughview/')

run_benchmark(benchmark)
