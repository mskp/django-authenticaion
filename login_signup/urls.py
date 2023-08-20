from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", include('auth_app.urls')),
    path("signup/", include('auth_app.urls')),
    path('', include('auth_app.urls')),
]
