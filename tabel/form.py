from django import forms
#from django.db import models
#from django.forms.models import ModelForm
from .models import tabel

class tabelForm(forms.ModelForm) :
    class Meta:
        model = tabel
        fields = ['waktu','nama', 'level', 'pesan']


