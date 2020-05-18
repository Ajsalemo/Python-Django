"""Forms for the User page"""
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from .

class UserCreationForm(UserCreationForm):
    username = TextInput

    class meta:
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
        }