from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def home(request):
    return HttpResponse("First Page Test and connection")

def not_home(request):
    name="Hello"
    return render(request,'FIRSTAPPLICATION/home.html')
def signup(request):
    name="SignUp"
    return render(request,'FIRSTAPPLICATION/Signup.html')

def signup2(request):
    #templet tagging
    calling_form=forms.Signupforms
    return render(request,'FIRSTAPPLICATION/Signup2.html',{'form':calling_form})

    