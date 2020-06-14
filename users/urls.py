"""URL mapping for "todo" tasks"""
from django.contrib.auth import views as auth_views
from django.urls import path

from users.views import register

from .forms import UserLoginForm

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html",
                                                authentication_form=UserLoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="index/index.html"), name="logout")
]
