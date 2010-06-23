from djangobench.utils import run_benchmark
from query_order_by.models import Book

def benchmark():
    list(Book.objects.order_by('id'))

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.order_by() call.',
    }
)
