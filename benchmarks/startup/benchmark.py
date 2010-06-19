from utils import run_benchmark

def benchmark():
    # Make sure the models and settings are loaded, then we're done. Calling
    # get_models() will make sure settings get loaded.
    from django.db import models
    models.get_models()
    
run_benchmark(benchmark)
