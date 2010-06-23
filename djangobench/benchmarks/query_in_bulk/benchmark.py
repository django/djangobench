from djangobench.utils import run_benchmark
from query_in_bulk.models import Book

def benchmark():
    Book.objects.in_bulk([1]) 

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.in_bulk() call.',
    }
)
