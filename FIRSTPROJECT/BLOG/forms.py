from django.forms import ModelForm
from .models import Regsistration,BlogRegsistration
from django import forms
from django.contrib.auth import authenticate, login


class Regsistration_form(ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Regsistration
        #fields = ['username','password','email','phone_number']
        fields = "__all__"
        widgets = {'password': forms.PasswordInput()}



class Blog_form(ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = BlogRegsistration
        #fields = ['username','password','email','phone_number']
        fields = "__all__"
        
class login_form(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        usernamex = self.cleaned_data.get("username")
        passwordx = self.cleaned_data.get("password")

        # if usernamex and passwordx:
        #     user = authenticate(username=usernamex, password=passwordx)
        #     if not user:
        #         raise forms.ValidationError("Username does not exists")
        #     else:
        #         id = Regsistration.objects.get(username=usernamex)
        #         if passwordx == Regsistration.password:
        #             raise form.ValidationError("Welcome!@")
        #         raise forms.ValidationError("Wrong Password")
        # else:
        #     raise form.ValidationError("Enter Username and Password to be validated")  


class Login_form2(ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Regsistration
        fields = ['username','password']
        
        widgets = {'password': forms.PasswordInput()}

class create_blog(Regsistration):
    
    class meta: