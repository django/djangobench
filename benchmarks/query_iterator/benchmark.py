import time

from utils import run_benchmark

from query_iterator.models import Book

fixtures = ['books']

def benchmark():
    Book.objects.iterator()

run_benchmark(benchmark)
