from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_in_bulk.models import Book

def benchmark():
    global Book
    Book.objects.in_bulk([1]) 

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.objects.in_bulk() call.',
    }
)
