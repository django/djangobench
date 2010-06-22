from djangobench.utils import run_benchmark
from query_iterator.models import Book

def benchmark():
    for i in Book.objects.iterator():
        pass

run_benchmark(benchmark, trials=50)
