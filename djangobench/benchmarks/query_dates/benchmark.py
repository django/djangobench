from djangobench.utils import run_benchmark

def setup():
    global Book
    from query_dates.models import Book

def benchmark():
    global Book
    list(Book.objects.dates("created_date", "year", "ASC"))

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.dates() call.',
    }
)
