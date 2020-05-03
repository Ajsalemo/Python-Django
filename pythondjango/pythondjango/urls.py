"""pythondjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from index.views import index
from todo.views import todo, update_completion_todo, update_task_importance
from todo_important.views import (
    all_important_tasks,
    update_important_tasks_completion,
    update_task_self_importance
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('todo/', todo, name="todo"),
    path('todo/c/<int:pk>', update_completion_todo, name="todo_complete"),
    path('todo/i/<int:pk>', update_task_importance, name="todo_important"),
    path('todo/i_a/', all_important_tasks, name="todo_important_all"),
    path('todo/i_c/<int:pk>',
         update_important_tasks_completion,
         name="update_important_task_completion"),
    path('todo/i_u/<int:pk>',
         update_task_self_importance,
         name="update_task_self_importance")
]
