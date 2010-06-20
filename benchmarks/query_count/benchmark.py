import time

from utils import run_benchmark

from query_count.models import Book

def benchmark():
    Book.objects.count()

run_benchmark(benchmark)
