from django.db import models


class Phones(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    ram = models.PositiveIntegerField()
    storage = models.PositiveIntegerField()
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="phones/")
    battery = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2 )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    