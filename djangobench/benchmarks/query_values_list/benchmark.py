from djangobench.utils import run_benchmark
from query_values_list.models import Book

def benchmark():
    list(Book.objects.values_list('title'))

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.values_list() call.',
    }
)
