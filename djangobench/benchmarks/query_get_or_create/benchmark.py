import itertools
from djangobench.utils import run_benchmark

counter = itertools.count(1)

def setup():
    global Book
    from query_get_or_create.models import Book

def benchmark():
    global Book
    nextid = next(counter)

    # This will do a create ...
    Book.objects.get_or_create(id=nextid, defaults={'title': 'hi'})
    
    # ... and this a get.
    Book.objects.get_or_create(id=nextid, defaults={'title': 'hi'})

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A Model.objects.get_or_create() call, both for '
                       'existing and non-existing objects.',
    }
)
