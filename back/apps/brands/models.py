from django.db import models
import uuid


class Brands(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    name = models.CharField(
        max_length=30,
        unique=True
    )

    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        max_length=1000,
        blank=True
    )

    logo = models.ImageField(
        upload_to="brands/",
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
