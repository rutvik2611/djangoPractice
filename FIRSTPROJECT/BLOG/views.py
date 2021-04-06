from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import Regsistration_form,login_form,Login_form2
from . import views
from django.contrib.auth import authenticate, login
from .models import Regsistration
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Reg_Serializer
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
            return HttpResponse("Issue :" + str(passing.errors))

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
            return HttpResponse("Issue : " + str(passing.errors))

    except:
        return HttpResponse("Issue Other than validating")

    
    return HttpResponse("ID was: "+ str(obj_for_query.username))

def login2(request):
 
    form = login_form(request.POST or None)
    if form.is_valid():

        usernamex = form.cleaned_data.get("username")
        passwordx = form.cleaned_data.get("password")
        try:
            user = authenticate(username=usernamex, password=passwordx)
            if user is not None:
                # A backend authenticated the credentials
                return render(request,"BLOG/Re.html",{"d":form})
            else:
                # No backend authenticated the credentials
                return HttpResponse("Not a user")
    
        except:
            return HttpResponse("UserName Does Not Exist")
        
        

    return render(request, 'BLOG/login.html', {'passed_value': form})


def random(request):
    x = x = {
  "name": "John",
  "age": 30,  
}
    return JsonResponse(x)

class RegList(APIView):
    def get(self,request):
        passing_this=Regsistration.objects.all()
        S = Reg_Serializer(passing_this, many = True)
        return Response(S.data)

    def post(self, request, format=None):
        serializer = Reg_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)