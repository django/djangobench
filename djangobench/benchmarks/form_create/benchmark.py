from django import forms
from djangobench.utils import run_benchmark

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)

def benchmark():
    BookForm({'title': 'a'})

run_benchmark(benchmark, trials=50)
