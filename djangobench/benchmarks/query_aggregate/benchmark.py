from django.db.models import Count

from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_aggregate.models import Book

def benchmark():
    global Book
    Book.objects.all().aggregate(Count('title'))

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.aggregate() call.',
    }
)
