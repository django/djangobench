from djangobench.utils import run_benchmark
from model_save_existing.models import Book

def benchmark():
    b = Book.objects.get(id=1)
    for i in range(0, 30):
        b.save()

run_benchmark(
    benchmark,
    meta={
        'description': 'A simple Model.save() call, instance exists in DB.',
    },
    setup=lambda: Book.objects.create(id=1, title='Foo')
)
