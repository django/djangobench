import itertools
from djangobench.utils import run_benchmark
from query_get_or_create.models import Book

counter = itertools.count(1)

def benchmark():
    nextid = counter.next()
    
    # This will do a create ...
    Book.objects.get_or_create(id=nextid, defaults={'title': 'hi'})
    
    # ... and this a get.
    Book.objects.get_or_create(id=nextid, defaults={'title': 'hi'})

run_benchmark(benchmark, trials=25)
