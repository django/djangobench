import time

from utils import run_benchmark

from query_update.models import Book

def benchmark():
    Book.objects.all().update(title='z')

run_benchmark(benchmark, trials=50)
