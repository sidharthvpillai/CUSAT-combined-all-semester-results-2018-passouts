from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Roll number', max_length=100)