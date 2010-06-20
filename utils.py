from time import time


def run_benchmark(benchmark, syncdb=True, trials=1):
    if syncdb:
        from django.core.management import call_command
        call_command("syncdb", verbosity=0)
    
    for x in xrange(trials):
        start = time()
        benchmark()
        print time() - start
