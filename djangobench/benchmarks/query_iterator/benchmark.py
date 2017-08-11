from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_iterator.models import Book

def benchmark():
    global Book
    list(Book.objects.iterator())

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.iterator() call.',
    }
)
