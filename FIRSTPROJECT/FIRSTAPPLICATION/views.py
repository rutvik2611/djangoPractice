from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("First Page Test and connection")

def not_home(request):
    name="Hello"
    return render(request,'FIRSTAPPLICATION/home.html')
def signup(request):
    name="SignUp"
    return render(request,'FIRSTAPPLICATION/Signup.html')

    