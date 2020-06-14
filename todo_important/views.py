"""This view is for tasks listed as important"""
from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
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


@login_required
def all_important_tasks(request):
    """This renders all important tasks in its own pane"""
    # Retrieve the logged in user by ID
    user = User.objects.filter(pk=request.user.id).first()
    # Concatenate the first letter of the users 'first name' and 'last name'
    # to create text that can overlay the user's avatar
    first_name_char = request.user.first_name[0].capitalize()
    last_name_char = request.user.last_name[0].capitalize()
    first_and_last_initial = f"{first_name_char}{last_name_char}"

    todays_datetime_imp = date.today()
    list_all_important_tasks = Task.objects.filter(user=request.user, important="True").values(
        "todo", "id", "completed", "important", "due_date")
    complete_important_task_form_true = CompleteImportantTask()
    complete_important_task_form_false = UncompleteImportantTask()
    set_task_importance_true = UpdateImportantTask()
    set_task_importance_false = DowngradeTaskFromImportant()
    add_important_task_due_date = AddDueDateTodoImportant()
    find_important_task_count = Task.objects.filter(user=request.user, important="True").count()
    delete_imp_task_form = DeleteTask()
    create_important_task_form = CreateImportantTask(request.POST or None)
    if create_important_task_form.is_valid():
        created_important_todo = create_important_task_form.cleaned_data['todo']
        add_todo_model = Task(
            todo=created_important_todo, important=True, user=user)
        add_todo_model.save()
        return redirect("todo_important_all")
    return render(request, "todo_important/todo_important.html",
                  {"list_all_important_tasks": list_all_important_tasks,
                   "create_important_task_form": create_important_task_form,
                   "complete_important_task_form_true": complete_important_task_form_true,
                   "complete_important_task_form_false": complete_important_task_form_false,
                   "set_task_importance_true": set_task_importance_true,
                   "set_task_importance_false": set_task_importance_false,
                   "add_important_task_due_date": add_important_task_due_date,
                   "delete_imp_task_form": delete_imp_task_form,
                   "find_important_task_count": find_important_task_count,
                   "todays_datetime_imp": todays_datetime_imp,
                   "first_and_last_initial": first_and_last_initial})


@login_required
def update_important_tasks_completion(request, pk):
    """This view is to complete an important task"""

    update_important_task_completion = get_object_or_404(Task, pk=pk)
    complete_important_task_form_true = CompleteImportantTask(
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


@login_required
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


@login_required
def add_todo_date_important(request, pk):
    """This is to a set a date for a task"""

    set_todo_date_imp = get_object_or_404(Task, pk=pk)
    set_todo_date_imp_form = AddDueDateTodoImportant(
        request.POST or None, instance=set_todo_date_imp)

    if set_todo_date_imp_form.is_valid():
        set_todo_date_imp_form.save()
        return redirect("todo_important_all")

    return render(request, "todo_important_all/todo_important_all.html")


@login_required
def delete_important_task(request, pk):
    """This is to delete a task"""

    delete_imp_task = get_object_or_404(Task, pk=pk)
    delete_imp_task_form = DeleteTask(
        request.POST or None, instance=delete_imp_task)

    if delete_imp_task_form.is_valid():
        delete_imp_task.delete()
        return redirect("todo_important_all")

    return render(request, "todo_important_all/todo_important_all.html")
