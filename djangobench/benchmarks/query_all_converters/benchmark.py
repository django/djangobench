from djangobench.utils import run_benchmark


def benchmark():
    global Converters
    list(Converters.objects.iterator())

def setup():
    global Converters
    from query_all_converters.models import Converters
    for i in range(0, 100):
        Converters().save()

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.iterator() call for large number of objects and large number of fields.',
    }
)
