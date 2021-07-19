from django import forms

class TableForm(forms.Form):
    username = forms.CharField(max_length = 20)
    email = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 16)