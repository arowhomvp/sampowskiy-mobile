from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/", include("apps.news.urls")),
    path("api/", include("apps.users.urls")),
    path("api/", include("apps.brands.urls")),
    path("api/", include("apps.reviews.urls")),
    path("api/", include("apps.phones.urls")),
    path("api/", include("apps.favorites.urls")),
    path("api/", include("apps.notifications.urls"))
]
