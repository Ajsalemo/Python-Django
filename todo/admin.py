"""Registering the Task model with Django Admin"""
from django.contrib import admin

from .models import Task


admin.site.register(Task)
