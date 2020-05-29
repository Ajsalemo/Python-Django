"""Forms for the User page"""
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, EmailField, PasswordInput, TextInput

from .models import User


class UserCreateForm(UserCreationForm):
    """Form that creates a user"""
    username = CharField(max_length=50, min_length=2, widget=TextInput(attrs={
        "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4
                                text-white""",
        "placeholder": "Username",
    }))

    first_name = CharField(max_length=50, min_length=2, widget=TextInput(attrs={
        "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4
                                text-white""",
        "placeholder": "First Name",
    }))

    last_name = CharField(max_length=50, min_length=2, widget=TextInput(attrs={
        "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4
                                text-white""",
        "placeholder": "Last Name",
    }))

    email = EmailField(label="", widget=TextInput(attrs={
        "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4
                                text-white""",
        "placeholder": "Email",
        "type": "email"
    }))

    password1 = CharField(label="", max_length=50, min_length=8, widget=PasswordInput(attrs={
        "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4
                                text-white""",
        "placeholder": "Password",
        "type": "password"
    }))

    password2 = CharField(label="", max_length=50, min_length=8, widget=PasswordInput(attrs={
        "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4
                                text-white""",
        "placeholder": "Confirm Password",
        "type": "password"
    }))

    class meta:
        """Form that creates a user"""
        model = User
        fields = ("username", "first_name", "last_name",
                  "password1", "password2", "email")
        help_texts = {
            "username": None,
            "password1": None,
            "password2": None,
        }

    # Override the save function of the UserCreateForm to add custom fields to the User model
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    """Custom User login form"""

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = CharField(max_length=50, min_length=8, label="id_username", widget=TextInput(
        attrs={
            "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4
                                text-white""",
            "placeholder": "Username",
        }))

    password = CharField(max_length=50, min_length=8, label="id_password", widget=PasswordInput(
        attrs={
            "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 mb-4
                                text-white""",
            "placeholder": "Password",
        }))
