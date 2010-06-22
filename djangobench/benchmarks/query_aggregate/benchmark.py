from django.db.models import Count
from djangobench.utils import run_benchmark
from query_aggregate.models import Book

def benchmark():
    Book.objects.all().aggregate(Count('title'))

run_benchmark(benchmark, trials=50)
