"""User model"""
from django.db.models import Model, CharField, EmailField


class User(Model):
    """User model"""
    username = CharField(max_length=50, null=False, blank=False)
    email = EmailField(max_length=50, null=False, blank=False)
    password = CharField(max_length=50, null=False, blank=False)


    def __str__(self):
        return f"User: {self.username}, {self.email}, {self.password}"
