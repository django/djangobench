from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_distinct.models import Book

def benchmark():
    global Book
    list(Book.objects.distinct())

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.objects.distinct() call.',
    }
)
