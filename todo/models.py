"""Database models"""
from django.db.models import (
    IntegerField, CharField, DateField, BooleanField, ForeignKey, CASCADE, Model
)
from django.contrib.auth.models import User


class Task(Model):
    """Task model"""
    todo = CharField(max_length=200, blank=True, null=False)
    date = DateField(null=True, blank=True)
    due_date = DateField(null=True, blank=True)
    important = BooleanField(default=False, blank=True)
    completed = BooleanField(default=False, blank=True)
    user = ForeignKey(User, on_delete=CASCADE)
