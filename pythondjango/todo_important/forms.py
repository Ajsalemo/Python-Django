"""Forms that update or create important tasks"""
from django import forms

from todo.models import Task


class CreateImportantTask(forms.ModelForm):
    """This form creates a task marked as important"""

    class Meta:
        model = Task
        fields = ('todo', 'important')
        labels = {
            'todo': '',
            'important': '',
        }
        widgets = {
            'todo': forms.TextInput(
                attrs={
                    'class': """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0""",
                    'type': 'search',
                    'placeholder': 'Add a task',
                    'id': "create-important-task-form"
                }
            ),
            'important': forms.CheckboxInput(
                attrs={
                    'class': 'd-none',
                    'checked': True,
                }
            )
        }


class CompleteImportantTask(forms.ModelForm):
    """This form completes an important task"""

    class Meta:
        model = Task
        fields = ('completed', 'important')
        labels = {
            'completed': '',
            'important': '',
        }
        widgets = {
            'completed': forms.CheckboxInput(
                attrs={
                    'class': 'd-none',
                    'checked': True,
                    'id': id
                }
            ),
            'important': forms.CheckboxInput(
                attrs={
                    'class': 'd-none',
                    'checked': True,
                    'id': id
                }
            )
        }


class UncompleteImportantTask(forms.ModelForm):
    """This form marks an important task as uncomplete"""

    class Meta:
        model = Task
        fields = ('completed', 'important')
        labels = {
            'completed': '',
            'important': '',
        }
        widgets = {
            'completed': forms.CheckboxInput(
                attrs={
                    'class': 'd-none',
                    'checked': False,
                    'id': id
                }
            ),
            'important': forms.CheckboxInput(
                attrs={
                    'class': 'd-none',
                    'checked': True,
                    'id': id
                }
            )
        }


class UpdateImportantTask(forms.ModelForm):
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
                    'checked': True,
                    'id': id
                }
            )
        }


class DowngradeTaskFromImportant(forms.ModelForm):
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
                    'checked': False,
                    'id': id
                }
            )
        }


class AddDueDateTodoImportant(forms.ModelForm):
    """This is to a due date to a task"""

    class Meta:
        model = Task
        fields = ('due_date', 'important')
        labels = {
            'due_date': '',
            'important': ''
        }
        widgets = {
            'due_date': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'due_date',
                    'id': id
                }
            ),
            'important': forms.CheckboxInput(
                attrs={
                    'class': 'd-none',
                    'checked': True,
                    'id': id
                }
            )
        }
