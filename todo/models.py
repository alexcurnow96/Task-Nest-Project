from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Dennis Ivy - see Readme.md
# TASK MODEL
class Task(models.Model):
    #unique identifier for each task
    id = models.AutoField(primary_key=True)
    #foreign key to link task to a user
    user = models.ForeignKey(get_user_model(
    ), on_delete=models.CASCADE, null=True,
        blank=True, related_name='user_tasks')
    #title of the task, limited to 200 characters
    title = models.CharField(max_length=200)
    #description of the task - optional
    description = models.TextField(null=True, blank=True)
    #boolean field to mark task as completed or not
    completed = models.BooleanField(default=False)
    #timestamp for when the task was created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #string representation of the task
        return self.title

    class Meta:
        #order tasks by completion status (incomplete first)
        ordering = ['completed']


# COMMENT MODEL
class Comment(models.Model):
    #links comment to a specific task
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='comments')
    #links comment to the user who created it
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #the context of the comment
    text = models.TextField()
    #timestamp for when the comment was created
    created_at = models.DateTimeField(auto_now_add=True)
