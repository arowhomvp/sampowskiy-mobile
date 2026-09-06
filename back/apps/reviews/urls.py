from django.urls import path
from .views import reviews, reviews_detail

urlpatterns = [
    path("reviews/", reviews),
    path("reviews/<int:reviews_id>/", reviews_detail)
]