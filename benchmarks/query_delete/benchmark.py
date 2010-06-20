from utils import run_benchmark

from query_delete.models import Book

def benchmark():
    for b in Book.objects.all():
        b.delete()

run_benchmark(benchmark)
