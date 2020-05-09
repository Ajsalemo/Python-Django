"""Views file for the 'todo' dashboard"""
from datetime import date

from django.shortcuts import get_object_or_404, redirect, render

from .forms import (AddDueDateTodo, CreateTask, DeleteTask,
                    DowngradeTaskImportance, EditTaskCompletion,
                    EditTaskCompletionFalse, UpdateTaskToImportant)
from .models import Task


def todo(request):
    """view for the general tasks dashboard"""

    todays_datetime = date.today()
    print(todays_datetime)
    d_date = Task.objects.values('due_date')
    print(d_date)
    display_task = Task.objects.values(
        'todo', 'id', 'completed', 'important', 'due_date')
    edit_task_form = EditTaskCompletion()
    edit_task_form_false = EditTaskCompletionFalse()
    upgrade_task_important = UpdateTaskToImportant()
    downgrade_task_importance = DowngradeTaskImportance()
    add_due_date_todo = AddDueDateTodo()
    delete_general_task = DeleteTask()
    find_important_task_count = Task.objects.filter(important="True").count()
    if request.method == "POST":
        create_task_form = CreateTask(request.POST)
        if create_task_form.is_valid():
            create_task_form.save()
            return redirect('todo')
    else:
        create_task_form = CreateTask()
    return render(request, "todo/todo.html",
                  {"create_task_form": create_task_form,
                   "display_task": display_task,
                   "edit_task_form": edit_task_form,
                   "edit_task_form_false": edit_task_form_false,
                   "upgrade_task_important": upgrade_task_important,
                   "downgrade_task_importance": downgrade_task_importance,
                   "add_due_date_todo": add_due_date_todo,
                   "delete_general_task": delete_general_task,
                   "find_important_task_count": find_important_task_count,
                   "todays_datetime": todays_datetime})


def update_completion_todo(request, pk):
    """This view is to update the added task - this marks it as complete or incomplete"""

    update_completion = get_object_or_404(Task, pk=pk)
    update_completion_form_true = EditTaskCompletion(
        request.POST or None, instance=update_completion)
    update_completion_form_false = EditTaskCompletion(
        request.POST or None, instance=update_completion)

    if update_completion_form_true.is_valid():
        update_completion_form_true.save()
        return redirect('todo')

    if update_completion_form_false.is_valid():
        update_completion_form_false.save()
        return redirect('todo')

    return render(request, "todo/todo.html")


def update_task_importance(request, pk):
    """This is to update a tasks importance"""

    upgrade_task_importance = get_object_or_404(Task, pk=pk)
    upgrade_task_importance_form = UpdateTaskToImportant(
        request.POST or None, instance=upgrade_task_importance)
    downgrade_task_importance_form = DowngradeTaskImportance(
        request.POST or None, instance=upgrade_task_importance)

    if upgrade_task_importance_form.is_valid():
        upgrade_task_importance_form.save()
        return redirect('todo')

    if downgrade_task_importance_form.is_valid():
        downgrade_task_importance_form.save()
        return redirect('todo')

    return render(request, "todo/todo.html")


def add_todo_date(request, pk):
    """This is to a set a date for a task"""

    set_todo_date = get_object_or_404(Task, pk=pk)
    set_todo_date_form = AddDueDateTodo(
        request.POST or None, instance=set_todo_date)

    if set_todo_date_form.is_valid():
        set_todo_date_form.save()
        return redirect('todo')

    return render(request, "todo/todo.html")


def delete_task(request, pk):
    """This is to delete a task"""

    delete_general_task = get_object_or_404(Task, pk=pk)
    delete_general_task_form = DeleteTask(
        request.POST or None, instance=delete_general_task)

    if delete_general_task_form.is_valid():
        delete_general_task.delete()
        return redirect('todo')

    return render(request, "todo/todo.html")
