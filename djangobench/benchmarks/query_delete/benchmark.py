from djangobench.utils import run_benchmark

def setup():
    global Book
    from query_delete.models import Book
    for i in range(0, 10):
        Book.objects.create(title='hi')

def benchmark():
    global Book
    Book.objects.all().delete()

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'Delete an object via QuerySet.delete().',
    },
)
