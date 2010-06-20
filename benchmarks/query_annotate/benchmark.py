from django.db.models import Count

from utils import run_benchmark

from query_annotate.models import Book

def benchmark():
    Book.objects.values('title').annotate(books_total=Count('id'))

run_benchmark(benchmark)
