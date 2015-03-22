from djangobench.utils import run_benchmark
from django.db import connection

def benchmark():
    cursor = connection.cursor()
    cursor.execute("select field1 from raw_sql_onefield")
    list(cursor.fetchall())

def setup():
    from raw_sql.models import OneField
    for i in range(0, 10):
        OneField(field1=i).save()

run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A test for stressing direct SQL performance',
    }
)
