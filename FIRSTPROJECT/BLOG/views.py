from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Regsistration_form,login_form
from . import views
from django.contrib.auth import authenticate, login
from .models import Regsistration
# Create your views here.

# def signup(request):
#     return HttpResponse("Hey!")

def signup(request):
    passing = Regsistration_form()
    if request.method == "POST":
        passing = Regsistration_form(request.POST)
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


# def Welcome(request):
#     pass_obj = Regsistration.objects.all()
#     return render(request,"BLOG/Welcome.html",{"Registration":pass_obj})

def Show(request):
    pass_obj = Regsistration.objects.all()
    return render(request,"BLOG/show.html",{"employees":pass_obj})



def login(request):
    form = login_form(request.POST or None)
    if form.is_valid():

        usernamex = form.cleaned_data.get("username")
        passwordx = form.cleaned_data.get("password")

        passing = Regsistration(request.POST)
        obj = passing.objects.get(username=usernamex)
        if True:
           return HttpResponse("Try") 

    return render(request, 'BLOG/login.html', {'passed_value': form})