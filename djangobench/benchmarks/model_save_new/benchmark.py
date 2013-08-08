from djangobench.utils import run_benchmark
from model_save_new.models import Book

def benchmark():
    for i in range(0, 30):
        b = Book(id=i, title='Foo')
        b.save()

run_benchmark(
    benchmark,
    meta={
        'description': 'A simple Model.save() call, instance not in DB.',
    },
)
