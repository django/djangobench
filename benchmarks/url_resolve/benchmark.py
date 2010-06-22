from django.core.urlresolvers import resolve

from utils import run_benchmark

def benchmark():
    resolve('/basic/')
    resolve('/fallthroughview/')
    resolve('/replace/1')

run_benchmark(benchmark, trials=20)
