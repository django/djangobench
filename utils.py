from time import time


def run_benchmark(benchmark, syncdb=True, trials=1):
    if syncdb:
        from django.core.management import call_command
        call_command("syncdb")
    cum_diff = 0.0
    
    for x in xrange(trials):
        start = time()
        benchmark()
        cum_diff += time() - start
        
    print cum_diff
