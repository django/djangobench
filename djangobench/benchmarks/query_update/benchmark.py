from djangobench.utils import run_benchmark

def setup():
    global Book
    from query_update.models import Book

def benchmark():
    global Book
    Book.objects.all().update(title='z')

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple QuerySet.update().',
    }
)
