from djangobench.utils import run_benchmark
from query_dates.models import Book

def benchmark():
    list(Book.objects.dates("created_date", "year", "ASC"))

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.dates() call.',
    }
)
