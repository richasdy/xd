from os import name
from django import forms
from django.contrib.auth.models import User

from django.shortcuts import redirect
import logging

#class priceForm(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    #price = forms.IntegerField(label='Your name')#, max_length=100)

class profilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super(profilForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user    

class loggingform():
    logging.getLogger(name)

    def save(self, commit=True):
        logging.getLogger = self.cleaned

#class logForm(forms.ModelForm):
#    class Meta :
#        model = LOGGING
#        fields = ['name', 'levelname','message']


            
