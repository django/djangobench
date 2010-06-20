from form_is_valid.forms import BookForm
from utils import run_benchmark

def setup():
    global book_form
    book_form = BookForm({'title': 'a'})
    
def benchmark():
    global book_form
    book_form.is_valid()

run_benchmark(benchmark, setup=setup, trials=50)
