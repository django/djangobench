import time

from utils import run_benchmark

from queries.models import Book


def benchmark():
    for i in xrange(10):
        Book.objects.create(title=unicode(i))

run_benchmark(benchmark)
