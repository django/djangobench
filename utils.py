from time import time

def run_benchmark(benchmark, syncdb=True, setup=None, trials=1):
    """
    Run a benchmark a few times and report the results.
    
    Arguments:
        
        benchmark
            The benchmark callable. ``run_benchmark`` will time
            the executation of this function and report those times
            back to the harness. However, if ``benchmark`` returns
            a value, that result will reported instead of the
            raw timing.
            
        syncdb
            If True, a syncdb will be performed before running
            the benchmark.
            
        setup
            A function to be called before running the benchmark
            function(s).
            
        trials
            The number of times to run the benchmark function.
    """
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

def run_comparison_benchmark(benchmark_a, benchmark_b, syncdb=True, setup=None, trials=1):
    """
    Benchmark the difference between two functions.
    
    Arguments are as for ``run_benchmark``, except that this takes 2
    benchmark functions, an A and a B, and reports the difference between
    them.
    
    For example, you could use this to test the overhead of an ORM query
    versus a raw SQL query -- pass the ORM query as ``benchmark_a`` and the
    raw query as ``benchmark_b`` and this function will report the
    difference in time between them.
    
    For best results, the A function should be the more expensive one
    (otherwise djangobench will report results like "-1.2x slower", which
    is just confusing).    
    """
    if syncdb:
        from django.core.management import call_command
        call_command("syncdb", verbosity=0)

    if setup:
        setup()
        
    for x in xrange(trials):
        start_a = time()
        result_a = benchmark_a()
        result_a = result_a or time() - start_a
        
        start_b = time()
        result_b = benchmark_b()
        result_b = result_b or time() - start_b
        
        print result_a - result_b