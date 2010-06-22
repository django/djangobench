from djangobench.utils import run_benchmark
from query_select_related.models import Book

def benchmark():
    list(Book.objects.select_related())

run_benchmark(benchmark, trials=50)
