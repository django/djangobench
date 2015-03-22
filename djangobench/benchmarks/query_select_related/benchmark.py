from djangobench.utils import run_benchmark

def setup():
    global Book
    from query_select_related.models import Book

def benchmark():
    global Book
    for i in range(20):
        list(Book.objects.select_related('author'))

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.objects.select_related() call.',
    }
)
