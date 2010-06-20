from time import time


def run_benchmark(benchmark, syncdb=True):
    if syncdb:
        from django.core.management import call_command
        call_command("syncdb", verbosity=0)
    start = time()
    benchmark()
    print time() - start
