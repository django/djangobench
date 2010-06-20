from query_none.models import Book
from utils import run_benchmark

def benchmark():
    Book.objects.none()

run_benchmark(benchmark, trials=50)
