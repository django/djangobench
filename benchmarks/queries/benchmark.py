import time

from django.core.management import call_command

from utils import run_benchmark

from queries.models import Book


call_command("syncdb")

def benchmark():
    for i in xrange(10):
        Book.objects.create(title=unicode(i))

run_benchmark(benchmark)
