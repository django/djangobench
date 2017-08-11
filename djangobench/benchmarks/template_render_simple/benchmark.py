import os

from django import template

from djangobench.utils import run_benchmark


def benchmark():
    context = template.Context({
        'stuff': 'something'
    });
    t = template.Template('{{ stuff }}')
    t.render(context)

run_benchmark(
    benchmark,
    migrate = False,
    meta = {
        'description': 'Render an extremely simple template (from string)',
    }
)
