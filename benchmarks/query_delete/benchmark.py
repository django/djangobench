from utils import run_benchmark
from query_delete.models import Book

def setup():
    global books
    books = [Book.objects.create(title='hi') for i in range(50)]

def benchmark():
    global books
    books.pop().delete()

run_benchmark(benchmark, setup=setup, trials=50)
