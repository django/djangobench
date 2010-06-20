from query_exclude.models import Book
from utils import run_benchmark

def benchmark():
    list(Book.objects.exclude(id=1))

run_benchmark(benchmark, trials=50)
