"""Views file for the 'todo' dashboard"""

from django.shortcuts import render, redirect

from .forms import CreateTask, EditTaskCompletion, EditTaskCompletionFalse
from .models import Task


def todo(request, id=id):
    """Function for the 'todo' view - this does the following:
    If a request method is that of POST, pass the POST request to the Model form
    If the form is valid, then submit it
    Else, if the method is that of GET, retrieve all Task objects in the database
    Display the normal form"""

    display_task = Task.objects.values('todo', 'id', 'completed')
    print(display_task)
    if request.method == "POST":
        create_task_form = CreateTask(request.POST)
        edit_task_form = EditTaskCompletion(request.POST)
        edit_task_form_false = EditTaskCompletionFalse(request.POST)
        if create_task_form.is_valid():
            create_task_form.save()
            return redirect('todo')
    else:
        create_task_form = CreateTask()
        edit_task_form = EditTaskCompletion()
        edit_task_form_false = EditTaskCompletionFalse()
    return render(request, "todo/todo.html",
                  {"create_task_form": create_task_form,
                   "display_task": display_task,
                   "edit_task_form": edit_task_form,
                   "edit_task_form_false": edit_task_form_false})
