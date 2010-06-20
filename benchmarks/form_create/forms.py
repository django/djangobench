from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
