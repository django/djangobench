from query_select_related.models import Book
from utils import run_benchmark

def benchmark():
    list(Book.objects.select_related())

run_benchmark(benchmark, trials=50)
