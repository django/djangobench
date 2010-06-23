from djangobench.utils import run_benchmark
from query_iterator.models import Book

def benchmark():
    list(Book.objects.iterator())

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.iterator() call.',
    }
)
