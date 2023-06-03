from django import forms
from django.contrib.auth.models import *
from .models import *
class RegAdminForm(forms.Form):
    email= forms.EmailField( )
    username=forms.CharField()
    password=forms.CharField(label="Password",widget=forms.PasswordInput())



class RegAdminModelForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    class Meta:
        model=MyUser
        # fields='__all__'
        exclude=['password']