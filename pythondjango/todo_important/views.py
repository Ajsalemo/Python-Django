"""This view is for tasks listed as important"""
from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Task
from .forms import CreateImportantTask, CompleteImportantTask


def all_important_tasks(request):
    """This renders all important tasks in its own pane"""
    list_all_important_tasks = Task.objects.all()
    complete_important_task_form_true = CompleteImportantTask()
    if request.method == "POST":
        create_important_task_form = CreateImportantTask(request.POST)
        if create_important_task_form.is_valid():
            create_important_task_form.save()
            return redirect("todo_important_all")
    else:
        create_important_task_form = CreateImportantTask()
    return render(request, "todo_important/todo_important.html",
                  {"list_all_important_tasks": list_all_important_tasks,
                   "create_important_task_form": create_important_task_form,
                   "complete_important_task_form_true": complete_important_task_form_true})


def complete_important_tasks(request, pk):
    """This view is to complete an important task"""

    complete_important_task = get_object_or_404(Task, pk=pk)
    complete_important_task_form_true = CreateImportantTask(
        request.POST or None, instance=complete_important_task)

    if complete_important_task_form_true.is_valid():
        complete_important_task_form_true.save()
        return redirect("todo_important_all")

    return render(request, "todo_important/todo_important.html")
