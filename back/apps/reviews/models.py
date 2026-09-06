from django.db import models
from django.conf import settings

class Reviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    phone = models.ForeignKey("phones.Phone", on_delete=models.CASCADE, related_name="reviews"),
    rating = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
