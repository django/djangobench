import time
from djangobench.utils import run_benchmark
from model_delete.models import Book

def benchmark():
    b = Book.objects.create(title='hi')
    start = time.time()
    b.delete()
    return time.time() - start

run_benchmark(
    benchmark,
    meta = {
        'description': 'Delete an object via Model.delete().',
    }
)
