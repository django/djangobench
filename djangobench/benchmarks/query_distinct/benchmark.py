from query_distinct.models import Book
from utils import run_benchmark

def benchmark():
    list(Book.objects.distinct())

run_benchmark(benchmark, trials=50)
