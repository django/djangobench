from django.core.urlresolvers import resolve

from djangobench.utils import run_benchmark


def benchmark():
    resolve("/0/00/000/0000/00000/000000/0000000/00000000/leaf")

run_benchmark(
    benchmark,
    meta = {
        'description': 'URL resolution with long-flat list of patterns.',
    }
)
