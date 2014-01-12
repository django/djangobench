from django import forms
from djangobench.utils import run_benchmark


class BookForm(forms.Form):
    title = forms.CharField(max_length=100)

form = None


def setup():
    # Can't initialize a form during import as __init__ uses
    # ugettext
    global form
    form = BookForm({'title': 'hi'})


def benchmark():
    form.full_clean()

run_benchmark(
    benchmark,
    syncdb=False,
    meta={
        'description': 'Speed of a Form.clean call.',
    },
    setup=setup
)
