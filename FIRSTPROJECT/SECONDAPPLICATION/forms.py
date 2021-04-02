from django.forms import ModelForm
from .models import register,Employee

class registration_form(ModelForm):
    
    class Meta:
        model = register
        fields = "__all__"

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
