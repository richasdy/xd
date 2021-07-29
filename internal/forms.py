from internal.models import TableModel
from django import forms
from django.db.models.base import Model
from django.forms import fields

class TableForm(forms.ModelForm):
    username = forms.CharField(max_length = 20)
    email = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 16)

    class Meta:
        model = TableModel
        fields = ['username', 'email', 'password']