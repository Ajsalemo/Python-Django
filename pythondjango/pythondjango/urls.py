"""URL mapping"""
from django.contrib import admin
from django.urls import path, include
from index.views import index
from todo.views import todo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("todo/", todo, name="todo"),
    path("todo/api/", include("todo.urls")),
    path("todo/important/", include("todo_important.urls")),
    path("auth/", include("users.urls"))
]
