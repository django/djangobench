from djangobench.utils import run_benchmark

def setup():
    global Book
    from query_exclude.models import Book

def benchmark():
    global Book
    list(Book.objects.exclude(id=1))

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.exclude() call.',
    }
)
