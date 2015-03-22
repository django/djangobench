from djangobench.utils import run_benchmark

def setup():
    global Book
    from query_values.models import Book

def benchmark():
    global Book
    list(Book.objects.values('title'))

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.values() call.',
    }
)
