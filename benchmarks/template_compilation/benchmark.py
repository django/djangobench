from django.template import Template

from utils import run_benchmark


def benchmark():
    # Just compile the template, no rendering
    t = Template("""
        {% for v in vals %}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
            {{ v }}
        {% endfor %}
    """)

run_benchmark(benchmark, syncdb=False, trials=100)
