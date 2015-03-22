from djangobench.utils import run_benchmark

def setup():
    global Book
    from query_complex_filter.models import Book

def benchmark():
    global Book
    Book.objects.complex_filter({'pk': 1})

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.complex_filter() call.',
    }
)
