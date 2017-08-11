from djangobench.utils import run_benchmark


def setup():
    global Book
    from model_creation.models import Book

def benchmark():
    global Book
    Book.objects.create(title='hi!')

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'Time of a Model.objects.create() call.',
    }
)
