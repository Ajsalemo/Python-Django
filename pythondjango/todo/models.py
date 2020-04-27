from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"User: {self.name}"


class Task(models.Model):
    todo = models.CharField(max_length=300)
    date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    important = models.BooleanField(default=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"Added the following: {self.todo}, {self.date}, {self.important}, {self.completed}"
