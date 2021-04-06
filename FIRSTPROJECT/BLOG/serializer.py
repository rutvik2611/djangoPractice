from rest_framework import serializers
from .models import Regsistration

class Reg_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Regsistration
        fields = "__all__"