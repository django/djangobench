from djangobench.utils import run_benchmark


def benchmark():
    global Book
    list(Book.objects.iterator())

def setup():
    global Book
    from query_all.models import Book
    for i in range(0, 3000):
        Book(pk=i, title='foobar_%s' % i).save()

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.objects.iterator() call for large number of objects.',
    }
)
