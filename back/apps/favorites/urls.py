from django.urls import path
from .views import favorites, favorites_details

urlpatterns = [
    path("favorites/", favorites),
    path("favorites/<int:favorites_id>/", favorites_details)
]