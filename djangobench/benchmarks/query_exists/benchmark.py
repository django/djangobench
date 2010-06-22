from djangobench.utils import run_benchmark
from query_exists.models import Book

def benchmark():
    #Checking for object that exists
    Book.objects.filter(id=1).exists()

    #Checking for object that does not exist
    Book.objects.filter(id=11).exists()

if hasattr(Book.objects, 'exists'):
    run_benchmark(benchmark, trials=50)
else:
    print "SKIP: Django before 1.2 doesn't have QuerySet.exists()"