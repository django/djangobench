from djangobench.utils import run_benchmark
from query_exclude.models import Book

def benchmark():
    list(Book.objects.exclude(id=1))

run_benchmark(benchmark, trials=50)
