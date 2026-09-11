from rest_framework import serializers
from .models import Phones

class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = "__all__"