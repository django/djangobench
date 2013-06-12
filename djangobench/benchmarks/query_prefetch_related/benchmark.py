from djangobench.utils import run_benchmark
from django import VERSION
from query_prefetch_related.models import Book, Author

def benchmark():
    for i in xrange(10):
        for a in Author.objects.prefetch_related('books'):
            list(a.books.all())

def setup():
    for i in range(0, 20):
        a = Author.objects.create(author="Author %s" % i)
        bset = set()
        for j in range(0, 3):
            b = Book.objects.create(title="Title %s" % j)
            bset.add(b)
        a.books = bset

if VERSION < (1, 4):
    print("SKIP: prefetch_related not supported before Django 1.4")
else:
    run_benchmark(
        benchmark,
        setup=setup,
        meta = {
            'description': 'A simple Model.objects.select_related() call.',
        }
    )
