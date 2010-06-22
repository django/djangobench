from django import forms
from djangobench.utils import run_benchmark

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)

form = BookForm({'title': 'hi'})

run_benchmark(form.full_clean, trials=50)
