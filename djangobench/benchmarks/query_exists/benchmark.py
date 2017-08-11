from django.db.models import Manager

from djangobench.utils import run_benchmark


def setup():
    global Book
    from query_exists.models import Book

def benchmark():
    global Book
    #Checking for object that exists
    Book.objects.filter(id=1).exists()

    #Checking for object that does not exist
    Book.objects.filter(id=11).exists()

if hasattr(Manager, 'exists'):
    run_benchmark(
        benchmark,
        setup=setup,
        meta={
            'description': 'A Model.objects.exists() call for both existing and non-existing objects.'
        }
    )
else:
    print("SKIP: Django before 1.2 doesn't have QuerySet.exists()")
