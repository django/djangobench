from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from djangobench.utils import run_benchmark

def form_validator(title):
    if title != 'hi':
        raise ValidationError(
            _('%(title)s is not equal to hi'),
            params={'title': title},
        )

class BookForm(forms.Form):
    title = forms.CharField(max_length=100, validators=[])

form = None

def setup():
    global form
    form = BookForm({'title':'hi'})

def benchmark():
    form.is_valid()

run_benchmark(
    benchmark,
    migrate=False,
    meta = {
        'description' : 'speed of form validation'
    },
    setup=setup
)