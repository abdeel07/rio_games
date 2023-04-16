from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('Logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('login/', auth_views.LoginView.as_view(template_name='Login.html'), name='Login'),
]