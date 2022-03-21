from django.db import connection

from djangobench.utils import run_comparison_benchmark


def setup():
    global Book
    from orm_vs_cursor_exec.models import Book
    for i in range(0, 300):
        Book(title=f"book_{i}").save()

def benchmark_orm():
    global Book
    from orm_vs_cursor_exec.models import Book
    Book.objects.all()


def benchmark_cursor_exec():
    cursor = connection.cursor()
    cursor.execute(
        "select * from book"
    )
    list(cursor.fetchall())

run_comparison_benchmark(
    benchmark_orm,
    benchmark_cursor_exec,
    setup=setup,
    meta={
        'description': 'Overhead of ORM compared to cursor.execute()'
    }
)
