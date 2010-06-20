from utils import run_benchmark

from query_get_or_create.models import Book

def benchmark():
    Book.objects.get_or_create(id=1)

run_benchmark(benchmark)
