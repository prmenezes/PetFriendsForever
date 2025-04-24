from django.urls import path
from .views import RegisterView
from django.contrib.auth import views


urlpatterns = [
    path("register/", RegisterView.as_view() , name="register_user"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]