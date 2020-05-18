"""User signup and login view"""
from django.shortcuts import render
from .forms import UserCreateForm


def register(request):
    """Provide users a form to register for the application"""
    userCreationForm = UserCreateForm()
    return render(request, "users/register.html", {"userCreationForm": userCreationForm})
