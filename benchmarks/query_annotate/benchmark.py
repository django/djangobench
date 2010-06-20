import time
from django.db.models import Count
from query_annotate.models import Book
from utils import run_benchmark

def benchmark():
    list(Book.objects.values('title').annotate(books_total=Count('id')))

run_benchmark(benchmark, trials=50)
