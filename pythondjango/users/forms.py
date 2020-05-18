"""Forms for the User page"""
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, EmailField
from .models import User


class UserCreateForm(UserCreationForm):
    """Form that creates a user"""
    username = CharField(max_length=50, min_length=2)
    email = EmailField()
    password1 = CharField(max_length=50, min_length=6)
    password2 = CharField(max_length=50, min_length=6)

    class meta:
        """Form that creates a user"""
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
