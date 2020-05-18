"""User signup and login view"""
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Provide users a form to register for the application"""
    userCreationForm = UserCreationForm()
    return render(request, "users/register.html", {"userCreationForm": userCreationForm})
