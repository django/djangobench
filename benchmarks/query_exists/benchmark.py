from utils import run_benchmark
from query_exists.models import Book

def benchmark():
    #Checking for object that exists
    Book.objects.filter(id=1).exists()

    #Checking for object that does not exist
    Book.objects.filter(id=11).exists()

run_benchmark(benchmark, trials=50)
