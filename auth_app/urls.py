from django.urls import path
from .views import login_view, signup_view, home, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('login', login_view, name='login'),
    path('signup', signup_view, name='signup'),
    path('logout', logout_view, name='logout'),
]