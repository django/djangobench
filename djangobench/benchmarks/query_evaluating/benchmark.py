from djangobench.utils import run_benchmark


def benchmark():
    global MultiField
    list(MultiField.objects.raw('select id from query_evaluating_multifield'))

def setup():
    global MultiField
    from query_evaluating.models import MultiField
    for i in range(0, 1000):
        kwargs = {}
        for j in range(1, 11):
            kwargs['field%s' % j] = 'foobar_%s_%s' % (i, j)
        MultiField(**kwargs).save()

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'Description': 'Evaluating the overall performance of the system.',
    }
)

