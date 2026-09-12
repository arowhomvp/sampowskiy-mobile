from django.urls import path
from .views import notifications, notifications_details

urlpatterns = [
    path("notifications/", notifications),
    path("notifications/<int:notification_id>/", notifications_details)
]