from django.template import Template, Context

from utils import run_benchmark

def benchmark():
    #Build a template, and render it
    t = Template("""
        Some text.
        {% for obj in objects %}
            {{ obj }}
            {{ obj }}
            {{ obj }}
            {{ obj }}
            {% if True %}
                {{ obj }}
            {% else %}
                {{ obj }}
            {% endif %}
        {% endfor %}
    """)

    objects = [object(), object(), object(), object(), object()]
    c = Context({'objects': objects})
    t.render(c)

for i in range(10):
    run_benchmark(benchmark, syncdb=False)
