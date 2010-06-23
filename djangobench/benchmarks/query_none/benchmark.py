from djangobench.utils import run_benchmark
from query_none.models import Book

def benchmark():
    list(Book.objects.none())

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.none() call.',
    }
)
