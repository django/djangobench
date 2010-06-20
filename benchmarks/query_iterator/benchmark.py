import time
from query_iterator.models import Book
from utils import run_benchmark

def benchmark():
    for i in Book.objects.iterator():
        pass

run_benchmark(benchmark, trials=50)
