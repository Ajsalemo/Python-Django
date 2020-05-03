"""Form that creates a task"""
from django import forms

from .models import Task


class CreateTask(forms.ModelForm):
    """This form is solely for creating tasks"""

    class Meta:
        model = Task
        fields = ('todo',)
        labels = {
            'todo': '',
        }
        widgets = {
            'todo': forms.TextInput(
                attrs={
                    'class': """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0""",
                    'type': 'search',
                    'placeholder': 'Add a task'
                }
            )
        }

class EditTaskCompletion(forms.ModelForm):
    """This is to edit the completion boolean field of a Task"""

    class Meta:
        model = Task
        fields = ('completed',)
        labels = {
            'completed': '',
        }
        widgets = {
            'completed': forms.CheckboxInput(
                attrs={
                    'class': 'd-none',
                    'checked': True
                }
            )
        }


class EditTaskCompletionFalse(forms.ModelForm):
    """This is to edit the completion boolean field of a Task"""

    class Meta:
        model = Task
        fields = ('completed',)
        labels = {
            'completed': '',
        }
        widgets = {
            'completed': forms.CheckboxInput(
                attrs={
                    'class': 'd-none',
                    'checked': False
                }
            )
        }


class UpdateTaskToImportant(forms.ModelForm):
    """This is to update a task to an 'important' status"""

    class Meta:
        model = Task
        fields = ('important',)
        labels = {
            'important': '',
        }
        widgets = {
            'important': forms.CheckboxInput(
                attrs={
                    'class': 'd-none',
                    'checked': True
                }
            )
        }

class DowngradeTaskImportance(forms.ModelForm):
    """This is to downgrade a task's importance'"""

    class Meta:
        model = Task
        fields = ('important',)
        labels = {
            'important': '',
        }
        widgets = {
            'important': forms.CheckboxInput(
                attrs={
                    'class': 'd-none',
                    'checked': False
                }
            )
        }
