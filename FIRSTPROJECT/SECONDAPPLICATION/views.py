from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.
# def home(request):

#     return HttpResponse("Hello Home")

def home(request):
    passing_form = forms.registration_form() #If i comment this out i get an error passing_form refered before intiating
    if request.method == "POST":
        passing_form = forms.registration_form(request.POST)
        if passing_form.is_valid():
            try:
                passing_form.save()
            except:
                print("Errorrr")
        else:
            passing_form = forms.registration_form() 
                       
    return render(request,'SECONDAPPLICATION/Registration.html',{'form':passing_form})
