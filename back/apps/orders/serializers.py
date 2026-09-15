from rest_framework import serializers
from .models import Orders, OrdersItem

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"
        read_only_fields = ["user"]

class OrdersItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersItem
        fields = "__all__"