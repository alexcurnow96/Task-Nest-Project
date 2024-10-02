# Code taken from Dennis Ivy (see ReadMe for details)

# Importing necessary modules and functions
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Task, Comment
from django.db.models import Q
from .forms import TaskForm, CommentForm

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from django.contrib import messages


# -----------------------TASK RELATED VIEWS -------------------------#
@login_required
def task_list(request):
    #retrieve tasks for the logged-in user
    tasks = Task.objects.filter(user=request.user)
    #count incomplete tasks
    count = tasks.filter(completed=False).count()

    context = {
        'tasks': tasks,
        'count': count,
    }
    return render(request, 'todo/task_list.html', context)


@login_required
def task_detail(request, pk):
    #get the specific task or return 404 if not found
    task = get_object_or_404(Task, pk=pk, user=request.user)
    #fetch all comments for the task
    comments = task.comments.all()  

    if request.method == 'POST':
        #handle comment submission
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user.id
            comment.save()
            return redirect('todo/task_detail.html', {'task': task})

    else:
        form = CommentForm()

    context = {
        'task': task,
        'form': form,
        'comments': comments,
    }
    return render(request, 'todo/task.html', context)


@login_required
def task_create(request):

    if request.method == 'POST':
        #handle task creation
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.add_message(request, messages.SUCCESS, "You have added a task to your list.")
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'todo/task_form.html', {'form': form})


@login_required
def task_update(request, pk):
    #get the object to update or return 404 if not found
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        #handle task update
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "You have updated a task on your list.")
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    context = {'form': form}
    return render(request, 'todo/task_form.html', context)


@login_required
def task_delete(request, pk):
    #get the task to delete or return 404 is not found
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        #handle task deletion
        task.delete()
        messages.success(request, "You have deleted a task from your list.")
        return redirect('task_list')

    return render(request, 'todo/task_confirm_delete.html', {'task': task})


@login_required
def toggle_task(request, task_pk):
    #toggle task completion status
    task = get_object_or_404(Task, pk=task_pk, project__user=request.user)
    task.completed = not task.completed
    task.save()
    messages.success(request, "You have completed a task on your list.")
    return redirect('project_detail', pk=task.project.pk)


# -----------------------COMMENT RELATED VIEWS -------------------------#

@login_required
def add_comment_to_task(request, pk):
    #get the task to add a comment to
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        #handle comment submission
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
            messages.success(request, "You have added a comment to your task.")
            return redirect('task_detail', pk=task.pk)
        else:
            form = CommentForm()

    return render(request, 'todo/task_detail.html', {'form': form, 'task': task})


@login_required
def delete_comment(request, comment_pk):
    #get the comment to delete or return a 404 if not found
    comment = get_object_or_404(Comment, pk=comment_pk)

    #check if the user had permission to delete the comment
    if comment.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this comment.")

    task_pk = comment.task.pk

    comment.delete()
    messages.success(request, "You have deleted a comment from your task.")

    return redirect('task_detail', pk=task_pk)

#index view
def index(request):
    return render(request, 'todo/index.html')


# TOGGLE TASK FOR CHECKLIST
@login_required
@require_POST
def toggle_task(request, task_id):
    task = Task.objects.get(id=task.id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'status': 'success', 'completed': task.completed})
