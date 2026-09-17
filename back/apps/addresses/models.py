from django.db import models
from apps.users.models import User


class Addresses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adresses")
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    building = models.CharField(max_length=20)
    apartment = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)