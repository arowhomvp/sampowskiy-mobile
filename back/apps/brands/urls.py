from django.urls import path
from .views import brands, brands_detail

urlpatterns = [
    path("brands/", brands),
    path("/brands/<uuid:brands_id>/", brands_detail)
]