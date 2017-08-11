from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_order_by.models import Book

def benchmark():
    global Book
    list(Book.objects.order_by('id'))

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.objects.order_by() call.',
    }
)
