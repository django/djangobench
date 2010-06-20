import time
from query_count.models import Book
from utils import run_benchmark

def benchmark():
    Book.objects.count()

run_benchmark(benchmark, trials=50)
