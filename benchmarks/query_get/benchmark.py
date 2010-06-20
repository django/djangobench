import time
from query_get.models import Book
from utils import run_benchmark

def benchmark():
    Book.objects.get(id=1)

run_benchmark(benchmark, trials=50)
