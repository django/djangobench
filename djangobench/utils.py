import argparse
import inspect
import time

benchmark_parser = argparse.ArgumentParser()
benchmark_parser.add_argument('-t', '--trials', type=int, default=100)

def run_benchmark(benchmark, syncdb=True, setup=None, trials=None, handle_argv=True, meta={}):
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
            The number of times to run the benchmark function. If not given
            and if ``handle_argv`` is ``True`` this'll be automatically
            determined from the ``--trials`` flag.
            
        handle_argv
            ``True`` if the script should handle ``sys.argv`` and set
            the number of trials accordingly.
            
        meta
            Key/value pairs to be returned as part of the benchmark results.
    """
    if handle_argv:
        args = benchmark_parser.parse_args()
        trials = trials or args.trials
    
    print_benchmark_header(benchmark, meta)
    
    if syncdb:
        from django.core.management import call_command
        call_command("syncdb", verbosity=0)
    
    if setup:
        setup()
    
    for x in xrange(trials):
        start = time.clock()
        benchmark_result = benchmark()

        if benchmark_result is not None:
            print benchmark_result
        else:
            print time.clock() - start

def run_comparison_benchmark(benchmark_a, benchmark_b, syncdb=True, setup=None, trials=None, handle_argv=True, meta={}):
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
    if handle_argv:
        args = benchmark_parser.parse_args()
        trials = trials or args.trials
    
    print_benchmark_header(benchmark_a, meta)
    
    if syncdb:
        from django.core.management import call_command
        call_command("syncdb", verbosity=0)

    if setup:
        setup()
        
    for x in xrange(trials):
        start_a = time.clock()
        result_a = benchmark_a()
        result_a = result_a or time.clock() - start_a
        
        start_b = time.clock()
        result_b = benchmark_b()
        result_b = result_b or time.clock() - start_b
        
        print result_a - result_b
        
def print_benchmark_header(benchmark, meta):
    if 'title' not in map(str.lower, meta.keys()):
        meta['title'] = inspect.getmodule(benchmark).__name__
    for key, value in meta.items():
        print '%s: %s' % (key.lower(), value)
    print