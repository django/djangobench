from form_create.forms import BookForm
from utils import run_benchmark

def benchmark():
    BookForm({'title': 'a'})

run_benchmark(benchmark, trials=50)
