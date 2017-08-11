from djangobench.utils import run_benchmark


def setup():
    global Book
    from model_save_existing.models import Book
    Book.objects.create(id=1, title='Foo')

def benchmark():
    global Book
    from model_save_existing.models import Book
    b = Book.objects.get(id=1)
    for i in range(0, 30):
        b.save()

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.save() call, instance exists in DB.',
    },
)
