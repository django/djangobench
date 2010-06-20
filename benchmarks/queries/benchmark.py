import time

from utils import run_benchmark

from queries.models import Book

def benchmark():
    Book.objects.create(title='hi!')

run_benchmark(benchmark, trials=50)
