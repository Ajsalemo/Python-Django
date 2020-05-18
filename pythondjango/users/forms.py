"""Forms for the User page"""
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, EmailField, TextInput

from .models import User


class UserCreateForm(UserCreationForm):
    """Form that creates a user"""
    username = CharField(max_length=50, min_length=2, label="", widget=TextInput(attrs={
        "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4 
                                text-center text-white""",
        "placeholder": "Username",
    }))

    email = EmailField(label="", widget=TextInput(attrs={
        "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4 
                                text-center text-white""",
        "placeholder": "Email"
    }))

    password1 = CharField(label="", max_length=50, min_length=6, widget=TextInput(attrs={
        "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4 
                                text-center text-white""",
        "placeholder": "Password"
    }))

    password2 = CharField(label="", max_length=50, min_length=6, widget=TextInput(attrs={
        "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4
                                text-center text-white""",
        "placeholder": "Confirm Password"
    }))

    class meta:
        """Form that creates a user"""
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            "username": None,
            "password1": None,
            "password2": None,
        }
