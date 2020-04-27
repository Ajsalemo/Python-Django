from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CreateTask
from .models import Task


def todo(request):
    if request.method == "POST":
        print(request.POST)
        create_task_form = CreateTask(request.POST)
        if create_task_form.is_valid():
            create_task_form.save()
    else:
        create_task_form = CreateTask()
    return render(request, "todo/todo.html", {"create_task_form": create_task_form})
