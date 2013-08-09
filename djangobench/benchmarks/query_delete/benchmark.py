from djangobench.utils import run_benchmark
from query_delete.models import Book

def benchmark():
    Book.objects.all().delete()

run_benchmark(
    benchmark,
    meta={
        'description': 'Delete an object via QuerySet.delete().',
    },
    setup=lambda: [Book.objects.create(title='hi') for i in range(0, 10)]
)
