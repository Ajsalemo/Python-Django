"""This view is for tasks listed as important"""
from django.shortcuts import render
from todo.models import Task


def all_important_tasks(request):
    """This renders all important tasks in its own pane"""
    list_all_important_tasks = Task.objects.all()
    print(list_all_important_tasks)
    return render(request, "todo_important/todo_important.html",
                  {"list_all_important_tasks": list_all_important_tasks})
