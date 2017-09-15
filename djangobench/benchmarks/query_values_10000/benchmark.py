from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_values_10000.models import Book
    Book.objects.bulk_create((
        Book(title='title')
        for x in range(10000)
    ))

def benchmark():
    global Book
    list(Book.objects.values('title'))

run_benchmark(
    benchmark,
    setup=setup,
)
