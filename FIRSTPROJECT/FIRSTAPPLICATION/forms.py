from django import forms
from django.core import validators

def check(value):
    #print(value)
    if len(value)<6:
        #print(type(value))
        raise forms.ValidationError("Should not be greater than 5")
       
            

class Signupforms(forms.Form):
    First_name=forms.CharField(label="First Name :")
    Last_name=forms.CharField(label="Last Name :")
    Email=forms.EmailField(max_length=40)
    psw=forms.CharField(widget=forms.PasswordInput, validators=[check])