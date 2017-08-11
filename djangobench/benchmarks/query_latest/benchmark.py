from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_latest.models import Book

def benchmark():
    global Book
    Book.objects.latest()

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.objects.latest() call.',
    }
)
