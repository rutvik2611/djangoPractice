from django.shortcuts import render
from django.http import HttpResponse
from .forms import LOGIN
# Create your views here.

# def signup(request):
#     return HttpResponse("Hey!")

def signup(request):
    if request.method == "POST":
        passing = LOGIN(request.POST)
        if passing.is_valid():
            try:
                passing.save()
                return HttpResponse0("views.signup")
            except:
                return HttpResponse("ERROR")
        else:
            passing = forms.LOGIN()
    return HttpResponse("WORKED I GUESS")