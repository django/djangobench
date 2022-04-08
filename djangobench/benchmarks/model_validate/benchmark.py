
from djangobench.utils import run_benchmark


def setup():
    global Book
    from model_validate.models import Book

def benchmark():
    global Book
    b = Book.objects.create(title="hi")
    b.full_clean()

run_benchmark(
    benchmark=benchmark,
    meta={
        'description' : 'Model validation benchmark'
    },
    setup=setup
)