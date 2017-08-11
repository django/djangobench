from django.core.urlresolvers import reverse

from djangobench.utils import run_benchmark


def benchmark():
    reverse('basic')
    reverse('catchall')
    reverse('vars', args=[1])
    reverse('vars', kwargs={'var': 1})

run_benchmark(
    benchmark,
    meta={
        'description': 'Reverse URL resolution.',
    }
)
