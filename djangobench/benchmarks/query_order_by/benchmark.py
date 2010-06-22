from query_order_by.models import Book
from utils import run_benchmark

def benchmark():
    list(Book.objects.order_by('id'))

run_benchmark(benchmark, trials=50)
