from query_values_list.models import Book
from utils import run_benchmark

def benchmark():
    list(Book.objects.values_list('title'))

run_benchmark(benchmark, trials=50)
