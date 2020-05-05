"""Views file for the 'todo' dashboard"""

from django.shortcuts import render, redirect, get_object_or_404

from .forms import (
    CreateTask,
    EditTaskCompletion,
    EditTaskCompletionFalse,
    UpdateTaskToImportant,
    DowngradeTaskImportance,
    AddDueDateTodo
)
from .models import Task


def todo(request):
    """Function for the 'todo' view - this does the following:
    If a request method is that of POST, pass the POST request to the Model form
    If the form is valid, then submit it
    Else, if the method is that of GET, retrieve all Task objects in the database
    Display the normal form"""

    display_task = Task.objects.values('todo', 'id', 'completed', 'important')
    edit_task_form = EditTaskCompletion()
    edit_task_form_false = EditTaskCompletionFalse()
    upgrade_task_important = UpdateTaskToImportant()
    downgrade_task_importance = DowngradeTaskImportance()
    add_due_date_todo = AddDueDateTodo()
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
                   "add_due_date_todo": add_due_date_todo})


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
