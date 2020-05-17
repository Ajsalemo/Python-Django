"""URL mapping for 'todo_important' tasks"""
from django.urls import path

from todo_important.views import (
    all_important_tasks,
    update_important_tasks_completion,
    update_task_self_importance,
    add_todo_date_important,
    delete_important_task
)

urlpatterns = [
    path('all/', all_important_tasks, name="todo_important_all"),
    path('complete/<int:pk>',
         update_important_tasks_completion,
         name="update_important_task_completion"),
    path('update/<int:pk>',
         update_task_self_importance,
         name="update_task_self_importance"),
    path('add_due_date/<int:pk>', add_todo_date_important,
         name="add_todo_date_imp"),
    path('delete/<int:pk>', delete_important_task, name="delete_important_task"),
]
