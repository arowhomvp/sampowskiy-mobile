from django.db import models
from apps.users.models import User
from django.conf import settings
from apps.phones.models import Phones

class Carts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="carts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

class CartsItem(models.Model):
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE, related_name="items")
    phone = models.ForeignKey(Phones, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        unique_together = ("cart", "phone")

    def __str__(self):
        return f"{self.quantity} x {self.phone} in Cart {self.cart_id}"