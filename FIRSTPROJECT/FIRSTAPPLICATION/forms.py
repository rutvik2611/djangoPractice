from django import forms

class Signupforms(forms.Form):
    First_name=forms.CharField(label="First Name :")
    Last_name=forms.CharField(label="Last Name :")
    Email=forms.EmailField(max_length=40)
    psw=forms.CharField(widget=forms.PasswordInput)