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

    return render(request,"BLOG/Registration.html",{"form":passing})


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
        try:

            passing = Regsistration.objects.get(username=usernamex)
            if passing.password != passwordx:
                return HttpResponse("Username and Password Did not Match") 
            else:
                return HttpResponse("Welcome :" + usernamex + " This is Your Email : " + passing.email + " This is your Phone Number: " + passing.phone_number)
    
        except:
            return HttpResponse("UserName Does Not Exist")
        
        

    return render(request, 'BLOG/login.html', {'passed_value': form})

def delete_registration(request,id):
    obj_for_query = Regsistration.objects.get(id=id)
    obj_for_query.delete()
    return redirect('../show')

def edit_registration(request,id):
    obj_for_query = Regsistration.objects.get(id=id)
    return render(request, 'BLOG/edit.html',{"employee":obj_for_query})

def update_registration(request,id):
    obj_for_query = Regsistration.objects.get(id=id)
    try:
        passing = Regsistration_form(request.POST, instance = obj_for_query)
        #print("threw Error")
        
        
        if passing.is_valid():
            print("validated")
            passing.save()
            print("Saved in Database")
            return redirect("../show")
        else:
            return HttpResponse("Possible Issue Username or Email Exists ,phonenumber does not meet our requirments")

    except:
        return HttpResponse("Issue Other than validating")

    
    return HttpResponse("ID was: "+ str(obj_for_query.username))