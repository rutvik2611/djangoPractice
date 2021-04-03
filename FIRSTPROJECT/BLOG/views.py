from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Regsistration
from . import views
# Create your views here.

# def signup(request):
#     return HttpResponse("Hey!")

def signup(request):
    passing = Regsistration()
    if request.method == "POST":
        passing = Regsistration(request.POST)
        if passing.is_valid():
            try:
                passing.save()
                #return HttpResponse("Registered")
                return redirect("welcome/") 
            except:
                return HttpResponse("ERROR")
        else:
            return HttpResponse("ERROR In Validating")

    return render(request,"BLOG/Registration.html",{"passed_value":passing})


def Welcome(request):
    return render(request,"BLOG/Welcome.html",{"Registration":Regsistration()})
    