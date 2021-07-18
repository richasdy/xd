from os import name
from django import forms
import tabel
#from django.contrib.auth.models import User

from django.shortcuts import redirect

#class priceForm(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    #price = forms.IntegerField(label='Your name')#, max_length=100)

class editForm(forms.ModelForm):
    class Meta:
        model = tabel
        fields = ['waktu','nama', 'level', 'pesan']

    def save(self, commit=True):
        tabel = super(editForm, self).save(commit=False)
        tabel.waktu = self.cleaned_data["waktu"]
        if commit:
            tabel.save()
        return tabel    

#class loggingform():
#    logging.getLogger(name)

#    def save(self, commit=True):
#        logging.getLogger = self.cleaned

#class logForm(forms.ModelForm):
#    class Meta :
#        model = LOGGING
#        fields = ['name', 'levelname','message']


            
