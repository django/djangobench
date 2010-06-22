from django.db.models import Count
from query_aggregate.models import Book
from utils import run_benchmark

def benchmark():
    Book.objects.all().aggregate(Count('title'))

run_benchmark(benchmark, trials=50)
