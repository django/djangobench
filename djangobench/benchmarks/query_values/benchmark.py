from query_values.models import Book
from utils import run_benchmark

def benchmark():
    list(Book.objects.values('title'))

run_benchmark(benchmark, trials=50)
