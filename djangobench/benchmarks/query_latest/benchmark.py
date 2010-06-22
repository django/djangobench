from djangobench.utils import run_benchmark
from query_latest.models import Book

def benchmark():
    Book.objects.latest()

run_benchmark(benchmark, trials=50)
