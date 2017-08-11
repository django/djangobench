import datetime

from djangobench.utils import run_benchmark


def setup():
    global Book
    from qs_filter_chaining.models import Book

def benchmark():
    global Book
    Book.objects.filter(title='Talent')\
                .filter(description__icontains='top performers')\
                .filter(author_name__startswith='Geoff')\
                .filter(date_created__lt=datetime.datetime(year=2010, month=1, day=1))\
                .filter(date_created__gte=datetime.date(year=2007, month=1, day=1))\
                .filter(date_published=datetime.datetime.now())\
                .filter(enabled=True)

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'Filter (but do not execute) a queryset mutliple times.',
    }
)
