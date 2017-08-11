from django.template import Template

from djangobench.utils import run_benchmark


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

run_benchmark(
    benchmark,
    migrate = False,
    meta = {
        'description': 'Template compilation time.',
    }
)
