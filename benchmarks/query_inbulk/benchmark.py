from query_inbulk.models import Book
from utils import run_benchmark

def benchmark():
    Book.objects.in_bulk([1]) 

run_benchmark(benchmark, trials=50)
