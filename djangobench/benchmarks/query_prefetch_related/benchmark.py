from django import VERSION

from djangobench.utils import run_benchmark


def benchmark():
    global Author
    for i in range(10):
        for a in Author.objects.prefetch_related('books'):
            list(a.books.all())


def setup():
    global Author
    from query_prefetch_related.models import Book, Author
    for i in range(0, 20):
        a = Author.objects.create(author="Author %s" % i)
        books = [Book.objects.create(title="Title %s" % j) for j in range(0, 3)]
        a.books.add(*books)

if VERSION < (1, 4):
    print("SKIP: prefetch_related not supported before Django 1.4")
else:
    run_benchmark(
        benchmark,
        setup=setup,
        meta={
            'description': 'A simple Model.objects.select_related() call.',
        }
    )
