"""User signup and login view"""
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserCreateForm


def register(request):
    """Provide users a form to register for the application"""
    userCreationForm = UserCreateForm(request.POST or None)
    if userCreationForm.is_valid():
        username = userCreationForm.cleaned_data.get("username")
        messages.success(request, f"Welcome, {username}. Please log in to continue.")
        userCreationForm.save()
        return redirect("login")
    return render(request, "users/register.html", {"userCreationForm": userCreationForm})
