from django.urls import path
from .views import carts, carts_details, items

urlpatterns = [
    path("carts/", carts),
    path("items/<int:item_id>", items),
    path("carts/<int:carts_id>/", carts_details)
]
