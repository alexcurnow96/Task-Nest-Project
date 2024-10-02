from django import forms
from .models import Task, Comment


class TaskForm(forms.ModelForm):
    class Meta:
        #specifices association with task model
        model = Task
        #lists the fields to include in the form
        fields = ['title', 'description', 'completed']


class CommentForm(forms.ModelForm):
    class Meta:
        #specifies association with comment model
        model = Comment
        #lists the fields to include in the form
        fields = ['text']
