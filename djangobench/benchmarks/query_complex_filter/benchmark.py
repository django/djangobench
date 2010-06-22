from query_complex_filter.models import Book
from utils import run_benchmark

def benchmark():
    Book.objects.complex_filter({'pk': 1})

run_benchmark(benchmark, trials=50)
