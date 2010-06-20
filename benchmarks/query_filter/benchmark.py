from utils import run_benchmark

from query_filter.models import Book

def benchmark():
    Book.objects.filter(id=1)

run_benchmark(benchmark)
