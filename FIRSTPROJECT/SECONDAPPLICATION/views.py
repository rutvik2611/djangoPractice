from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from FIRSTAPPLICATION import views as v # not needed
from .forms import EmployeeForm  #why did i need to import this sepratly
from .models import Employee
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
                return redirect(v.not_home) #just to check
            except:
                print("Errorrr")
        else:
            passing_form = forms.registration_form() 
                       
    return render(request,'SECONDAPPLICATION/Registration.html',{'form':passing_form})

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'SECONDAPPLICATION/index.html',{'form':form})

#READ
def show(request):
    employees=Employee.objects.all()
    return render(request, "SECONDAPPLICATION/show.html", {'employees':employees})

#DELETE, EDIT/UPDATE
def destroy(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')
    
#UPDATE--> EDIT -> UPDATE

def edit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'employee':employee})