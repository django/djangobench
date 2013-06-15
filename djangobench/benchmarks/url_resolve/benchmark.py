from django.core.urlresolvers import resolve
from djangobench.utils import run_benchmark

def benchmark():
    for i in range(0, 100):
        resolve('/basic/')
        resolve('/fallthroughview/')
        resolve('/replace/1')

run_benchmark(
    benchmark,
    meta = {
        'description': 'URL resolution.',
    }
)
