from django.urls import path
from .views import login, create
urlpatterns = [
    path("login/", login),
    path("register/", create)
]