from django.db import models
from django.conf import settings
from apps.phones.models import Phones


class Orders(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=22)
    address =  models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrdersItem(models.Model):
        order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="items")
        phone = models.ForeignKey(Phones, on_delete=models.PROTECT, related_name="order_item")
        quantity = models.SmallIntegerField(default=1)
        price  = models.DecimalField(max_digits=10, decimal_places=2)