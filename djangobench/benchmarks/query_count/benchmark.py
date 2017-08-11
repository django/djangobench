from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_count.models import Book

def benchmark():
    global Book
    Book.objects.count()

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.count() call.',
    }
)
