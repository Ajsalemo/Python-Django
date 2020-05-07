"""This view is for tasks listed as important"""
from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Task
from todo.forms import DeleteTask

from .forms import (
    CreateImportantTask,
    CompleteImportantTask,
    UncompleteImportantTask,
    UpdateImportantTask,
    DowngradeTaskFromImportant,
    AddDueDateTodoImportant
)

def all_important_tasks(request):
    """This renders all important tasks in its own pane"""
    list_all_important_tasks = Task.objects.all()
    complete_important_task_form_true = CompleteImportantTask()
    complete_important_task_form_false = UncompleteImportantTask()
    set_task_importance_true = UpdateImportantTask()
    set_task_importance_false = DowngradeTaskFromImportant()
    add_important_task_due_date = AddDueDateTodoImportant()
    delete_imp_task_form = DeleteTask()
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
                   "complete_important_task_form_true": complete_important_task_form_true,
                   "complete_important_task_form_false": complete_important_task_form_false,
                   "set_task_importance_true": set_task_importance_true,
                   "set_task_importance_false": set_task_importance_false,
                   "add_important_task_due_date": add_important_task_due_date,
                   "delete_imp_task_form": delete_imp_task_form})


def update_important_tasks_completion(request, pk):
    """This view is to complete an important task"""

    update_important_task_completion = get_object_or_404(Task, pk=pk)
    complete_important_task_form_true = CreateImportantTask(
        request.POST or None, instance=update_important_task_completion)
    complete_important_task_form_false = UncompleteImportantTask(
        request.POST or None, instance=update_important_task_completion)

    if complete_important_task_form_true.is_valid():
        complete_important_task_form_true.save()
        return redirect("todo_important_all")

    if complete_important_task_form_false.is_valid():
        complete_important_task_form_false.save()
        return redirect("todo_important_all")

    return render(request, "todo_important/todo_important.html")


def update_task_self_importance(request, pk):
    """This view is to update a tasks importance"""

    update_importance = get_object_or_404(Task, pk=pk)
    set_task_importance_true = UpdateImportantTask(
        request.POST or None, instance=update_importance)
    set_task_importance_false = DowngradeTaskFromImportant(
        request.POST or None, instance=update_importance)

    if set_task_importance_true.is_valid():
        set_task_importance_true.save()
        return redirect("todo_important_all")

    if set_task_importance_false.is_valid():
        set_task_importance_false.save()
        return redirect("todo_important_all")

    return render(request, "todo_important/todo_important.html")


def add_todo_date_important(request, pk):
    """This is to a set a date for a task"""

    set_todo_date_imp = get_object_or_404(Task, pk=pk)
    set_todo_date_imp_form = AddDueDateTodoImportant(
        request.POST or None, instance=set_todo_date_imp)

    if set_todo_date_imp_form.is_valid():
        set_todo_date_imp_form.save()
        return redirect('todo_important_all')

    return render(request, "todo_important_all/todo_important_all.html")


def delete_important_task(request, pk):
    """This is to delete a task"""

    delete_imp_task = get_object_or_404(Task, pk=pk)
    delete_imp_task_form = DeleteTask(
        request.POST or None, instance=delete_imp_task)

    if delete_imp_task_form.is_valid():
        delete_imp_task.delete()
        return redirect('todo_important_all')

    return render(request, "todo_important_all/todo_important_all.html")
