from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_get.models import Book

def benchmark():
    global Book
    # This will succeed
    Book.objects.get(id=1)
    try:
        # This will fail, due to too many objects
        Book.objects.get()
    except:
        pass

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.objects.get() call.',
    }
)
