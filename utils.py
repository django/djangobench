from time import time

def run_benchmark(benchmark, syncdb=True, setup=None, trials=1):
    if syncdb:
        from django.core.management import call_command
        call_command("syncdb", verbosity=0)
    
    if setup:
        setup()
    
    for x in xrange(trials):
        start = time()
        benchmark_result = benchmark()

        if benchmark_result is not None:
            print benchmark_result
        else:
            print time() - start
