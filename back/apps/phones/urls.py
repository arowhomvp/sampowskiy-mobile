from django.urls import path
from .views import phones, phones_detail

urlpatterns = [
    path("phones/", phones),
    path("phones/<int:phones_id>/", phones_detail)
]