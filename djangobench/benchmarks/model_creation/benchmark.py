import time
from djangobench.utils import run_benchmark
from model_creation.models import Book

def benchmark():
    Book.objects.create(title='hi!')

run_benchmark(benchmark, trials=50)