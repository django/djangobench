from django.db.models import Count

from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_annotate.models import Book

def benchmark():
    global Book
    list(Book.objects.values('title').annotate(books_total=Count('id')))

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.objects.annotate() call.',
    }
)
