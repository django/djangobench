from djangobench.utils import run_benchmark
from query_distinct.models import Book

def benchmark():
    list(Book.objects.distinct())

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.distinct() call.',
    }
)
