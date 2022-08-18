
from django import forms


class CarForm(forms.Form):
    title = forms.CharField(max_length=200)
    model = forms.CharField()
    color = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)