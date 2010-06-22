from djangobench.utils import run_benchmark
from query_filter.models import Book

def benchmark():
    list(Book.objects.filter(id=1))

run_benchmark(benchmark, trials=50)
