"""User model"""
from django.db.models import Model, CharField, IntegerField


class User(Model):
    """User model"""
    id = IntegerField(primary_key=True)
    username = CharField(max_length=50, null=False, blank=False)
    first_name = CharField(max_length=50, null=False, blank=False)
    last_name = CharField(max_length=100, null=False, blank=False)
    password = CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"User: {self.username}, {self.password}"
