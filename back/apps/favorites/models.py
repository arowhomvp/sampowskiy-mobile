from django.db import models
from apps.phones.models import Phones
from apps.users.models import User

class Favorites(models.Model):
    phone = models.ForeignKey(Phones, on_delete=models.CASCADE, related_name="favorites")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True)
