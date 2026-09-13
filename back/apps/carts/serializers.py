from rest_framework import serializers
from .models import Carts, CartsItem

class CartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        read_only_fields = ["user", "created_at", "updated_at"]

class CartsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartsItem
        fields = "__all__"