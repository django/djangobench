import time

from djangobench.utils import run_benchmark


def setup():
    global Book
    from model_delete.models import Book

def benchmark():
    global Book
    b = Book.objects.create(title='hi')
    start = time.time()
    b.delete()
    return time.time() - start

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'Delete an object via Model.delete().',
    }
)
