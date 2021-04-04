from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Regsistration
from . import views
from django.contrib.auth import authenticate, login
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
                return render(request,"BLOG/Welcome.html",{"Registration":passing})
            except:
                return HttpResponse("ERROR")
        else:
            return HttpResponse("ERROR In Validating")

    return render(request,"BLOG/Registration.html",{"passed_value":passing})


def Welcome(request):
    pass_obj = Regsistration.objects.all()
    return render(request,"BLOG/Welcome.html",{"Registration":pass_obj})



def login(request):
    form = login_form(request.POST or None)
    if form.is_valid():
       username = form.cleaned_data.get("username")
       password = form.cleaned_data.get("password")
       user = authenticate(username=username, password=password)
       login(request,user)
    return render(request, 'login.html', {'form': form})