from django.db.models import Count
from djangobench.utils import run_benchmark
from query_annotate.models import Book

def benchmark():
    list(Book.objects.values('title').annotate(books_total=Count('id')))

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.annotate() call.',
    }
)
