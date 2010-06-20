from query_dates.models import Book
from utils import run_benchmark

def benchmark():
    list(Book.objects.dates("created_date", "year", "ASC"))

run_benchmark(benchmark, trials=50)
