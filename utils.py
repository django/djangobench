from time import time


def run_benchmark(benchmark):
    start = time()
    benchmark()
    print time() - start
