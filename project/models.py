from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from todo.models import Task

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
