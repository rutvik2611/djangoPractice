from django.forms import ModelForm
from .models import register

class registration_form(ModelForm):
    
    class Meta:
        model = register
        fields = "__all__"