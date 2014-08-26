from djangobench.utils import run_benchmark
from query_all_converters.models import Converters

def benchmark():
    list(Converters.objects.iterator())

def setup():
    for i in range(0, 100):
        Converters().save()

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.iterator() call for large number of objects and large number of fields.',
    }
)
