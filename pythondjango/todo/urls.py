"""URL mapping for "todo" tasks"""
from django.urls import path
from todo.views import (
    update_completion_todo,
    update_task_importance,
    add_todo_date,
    delete_task
)

urlpatterns = [
    path("complete/<int:pk>", update_completion_todo, name="todo_complete"),
    path("important/<int:pk>", update_task_importance, name="todo_important"),
    path("due_date/<int:pk>", add_todo_date, name="add_todo_date"),
    path("delete/<int:pk>", delete_task, name="delete_task"),
]
