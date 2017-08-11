try:
    from django.urls import resolve
except ImportError:  # Django < 1.10
    from django.core.urlresolvers import resolve

from djangobench.utils import run_benchmark


def benchmark():
    paths = (
        '/user/repo/feature19',
        '/section0/feature0',
        '/en/feature10',
        '/ru/feature10',
        '/missing',
    )
    for i in range(0, 100):
        for path in paths:
            try:
                resolve(path)
            except:
                pass
run_benchmark(
    benchmark,
    meta={
        'description': 'URL resolution with long-flat list of patterns.',
    }
)
