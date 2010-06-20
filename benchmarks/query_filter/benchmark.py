from query_filter.models import Book
from utils import run_benchmark

def benchmark():
    list(Book.objects.filter(id=1))

run_benchmark(benchmark, trials=50)
