from django import forms
from django.core import validators
import re

def check(value):
    #print(value)
    if re.match("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",value):
        print("Validated")
    else:
        print("Password Validation Error")
        raise forms.ValidationError("Should not be greater than 5")
       
            

class Signupforms(forms.Form):
    First_name=forms.CharField(label="First Name :")
    Last_name=forms.CharField(label="Last Name :")
    Email=forms.EmailField(max_length=40)
    psw=forms.CharField(widget=forms.PasswordInput, validators=[check])