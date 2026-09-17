from django.urls import path
from .views import addresses, addresses_details

urlpatterns = [
    path("addresses/", addresses),
    path("addresses/<int:addresses_id>", addresses_details)
]