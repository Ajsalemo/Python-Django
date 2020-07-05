# Python-Django
An application using Python to test out the Django framework.

![Imgur](https://i.imgur.com/wDit6ku.png)

## Login and Sign up
To access the application, sign up by creating an account, afterwards you'll be able to log in

## Tasks/Todos
Tasks and todos are the same concept. You can create a task which is set without any due date, importance or completion mark.

### Due date
A due date can be set for a task which will appear underneath the task's text. A due date cannot be set in the past. If a due date is past due, it will turn red. A due date can be updated at any time.

### Importance
A task can be marked as important, the star icon will appear solid when important and only an outline showing when it has non-importance.

### Completion
When a task if marked as completed(by clicking the circle to the left of the task), a strikethough will go through the task's text, marking it as complete.

## Important tasks by default
Tasks created under the 'Important tasks' view will be marked as important by default.

## Delete
Tasks can be deleted from either the normal or 'important' dashboard.

## Accounts
Accounts are created with Djangos built-in authentication with validation included. Accounts are case sensitive. Currently they only serve the purpose as to access your stored tasks, no other customization has been added yet.

