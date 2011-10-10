from djangobench.utils import run_benchmark
from query_select_related.models import Book

def benchmark():
    for i in xrange(20):
        list(Book.objects.select_related('author'))

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.select_related() call.',
    }
)
