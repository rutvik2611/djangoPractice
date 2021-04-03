from django.forms import ModelForm
from .models import Regsistration
from django import forms

class Regsistration(ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Regsistration
        #fields = ['username','password','email','phone_number']
        fields = "__all__"
        widgets = {'password': forms.PasswordInput()}

    
