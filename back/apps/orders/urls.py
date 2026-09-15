from django.urls import path
from .views import orders, orders_details, orders_items, orders_item_details

urlpatterns = [
    path("orders/", orders),
    path("orders/<int:orders_id>/", orders_details),
    path("orders/<int:orders_id>/items/", orders_items),
    path("orders/<int:orders_id>/items/<int:item_id>/", orders_item_details)
]