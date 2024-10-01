from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.


# Dennis Ivy - see Readme.md

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(
    ), on_delete=models.CASCADE, null=True, blank=True, related_name='user_tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']


# COMMENT MODEL _ PLEASE WORK
class Comment(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
