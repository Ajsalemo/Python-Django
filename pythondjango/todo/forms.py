"""Form that creates, edits, or updates a task"""
from datetime import date
from django.forms import ModelForm, TextInput, CheckboxInput, DateInput, ValidationError
from .models import Task


class CreateTask(ModelForm):
    """This form is solely for creating tasks"""

    class Meta:
        model = Task
        fields = ("todo",)
        widgets = {
            "todo": TextInput(
                attrs={
                    "class": """form-control rounded-0 mr-sm-2 todo-page-add-task-form-input
                                border-top-0 border-right-0 border-left-0 text-white""",
                    "type": "search",
                    "placeholder": "Add a task",
                    "id": "create-task-form"
                }
            )
        }

        


class EditTaskCompletion(ModelForm):
    """This is to edit the completion boolean field of a Task"""

    class Meta:
        model = Task
        fields = ("completed",)
        labels = {
            "completed": "",
        }
        widgets = {
            "completed": CheckboxInput(
                attrs={
                    "class": "d-none",
                    "checked": True,
                    "id": id
                }
            )
        }


class EditTaskCompletionFalse(ModelForm):
    """This is to edit the completion boolean field of a Task"""

    class Meta:
        model = Task
        fields = ("completed",)
        labels = {
            "completed": "",
        }
        widgets = {
            "completed": CheckboxInput(
                attrs={
                    "class": "d-none",
                    "checked": False,
                    "id": id
                }
            )
        }


class UpdateTaskToImportant(ModelForm):
    """This is to update a task to an "important" status"""

    class Meta:
        model = Task
        fields = ("important",)
        labels = {
            "important": "",
        }
        widgets = {
            "important": CheckboxInput(
                attrs={
                    "class": "d-none",
                    "checked": True,
                    "id": id
                }
            )
        }


class DowngradeTaskImportance(ModelForm):
    """This is to downgrade a task's importance"""

    class Meta:
        model = Task
        fields = ("important",)
        labels = {
            "important": "",
        }
        widgets = {
            "important": CheckboxInput(
                attrs={
                    "class": "d-none",
                    "checked": False,
                    "id": id
                }
            )
        }


class AddDueDateTodo(ModelForm):
    """This is to a due date to a task"""

    class Meta:
        model = Task
        fields = ("due_date",)
        labels = {
            "due_date": "",
        }
        widgets = {
            "due_date": DateInput(
                attrs={
                    "class": "due_date",
                    "id": id
                }
            )
        }

    def clean_due_date(self):
        """This prevents a past date from being entered for a Task due date"""
        due_date = self.cleaned_data.get("due_date")
        if due_date is None:
            pass
        elif due_date < date.today():
            raise ValidationError("Meetings cannot be in the past")
        return due_date


class DeleteTask(ModelForm):
    """This is to delete a task"""

    class Meta:
        model = Task
        fields = []

