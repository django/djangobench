# XXX FIXME - has to spawn a new process to measure load time

from django import VERSION

from djangobench.utils import run_benchmark


def benchmark():
    # Make sure the models and settings are loaded, then we're done. Calling
    # get_models() will make sure settings get loaded.
    from django.db import models
    models.get_models()

if VERSION < (1, 9):
    run_benchmark(
        benchmark,
        migrate = False,
        trials = 1,
        meta = {
            'description': 'Startup time for a simple app.',
        }
    )
else:
    print("SKIP: Django 1.9 and later has changed app loading. This benchmark needs fixing anyway.")
