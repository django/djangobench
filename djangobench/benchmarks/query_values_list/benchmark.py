from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_values_list.models import Book

def benchmark():
    global Book
    list(Book.objects.values_list('title'))

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.values_list() call.',
    }
)
