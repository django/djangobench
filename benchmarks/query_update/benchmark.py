from query_update.models import Book
from utils import run_benchmark

def benchmark():
    Book.objects.all().update(title='z')

run_benchmark(benchmark, trials=50)
