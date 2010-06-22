from djangobench.utils import run_benchmark
from query_values_list.models import Book

def benchmark():
    list(Book.objects.values_list('title'))

run_benchmark(benchmark, trials=50)
