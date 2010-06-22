from djangobench.utils import run_benchmark
from query_values.models import Book

def benchmark():
    list(Book.objects.values('title'))

run_benchmark(benchmark, trials=50)
