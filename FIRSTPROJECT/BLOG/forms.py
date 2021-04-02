from django.forms import ModelForm
from .models import LOGIN

class LOGIN(ModelForm):

    class Meta:
        model = LOGIN
        fields = "__all__"

    
