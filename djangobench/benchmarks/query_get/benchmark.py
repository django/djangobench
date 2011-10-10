from djangobench.utils import run_benchmark
from query_get.models import Book

def benchmark():
    for i in range(0, 30):
        # This will succeed
        Book.objects.get(id=1)
        try:
            # This will fail, due to too many objects
            Book.objects.get()
        except:
            pass

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.get() call.',
    }
)
