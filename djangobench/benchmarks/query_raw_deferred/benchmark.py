from djangobench.utils import run_benchmark


def benchmark():
    global MultiField
    list(MultiField.objects.raw('select id from query_raw_deferred_multifield'))

def setup():
    global MultiField
    from query_raw_deferred.models import MultiField
    for i in range(0, 1000):
        kwargs = {}
        for j in range(1, 11):
            kwargs['field%s' % j] = 'foobar_%s_%s' % (i, j)
        MultiField(**kwargs).save() 

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A test for fetching large number of objects by Model.objects.all() with deferred fields.',
    }
)
