from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_filter.models import Book

def benchmark():
    global Book
    list(Book.objects.filter(id=1))

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.objects.filter() call.',
    }
)
