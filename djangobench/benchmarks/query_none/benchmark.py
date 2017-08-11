from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_none.models import Book

def benchmark():
    global Book
    list(Book.objects.none())

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.objects.none() call.',
    }
)
