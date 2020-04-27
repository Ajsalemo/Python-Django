from django import forms

from .models import Task


class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('todo',)
        labels = {
            'todo': '',
        }
        widgets = {
            'todo': forms.TextInput(
                attrs={
                    'class': 'form-control rounded-0 mr-sm-2 todo-page-add-task-form-input border-top-0 border-right-0 border-left-0',
                    'type': 'search',
                }
            )
        }
