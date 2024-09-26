# Code taken from Dennis Ivy (see ReadMe for details)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
from .models import Task, Project
from django.db.models import Q



#-----------------------TASKS-------------------------#
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    count = tasks.filter(complete=False).count()

    context = {
        'tasks': tasks,
        'count': count,
    }
    return render(request, 'todo/task_list.html', context)

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'todo/task.html', {'task': task})

def task_create(request, project_id):
    project = get_object_or_404(Project, id=project.id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.project = project
            task.save()
            return redirect('task-create', project_id=project.id)
    else:
        form = TaskForm()

    return render(request, 'task-form.html', {'form': form, 'project': project})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    project = task.project 

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.project = project 
            task.save()
            return redirect('project_detail', project_id=project.id)

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    project = task.project 

    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', project_id=project.id)

    return render(request, 'task_confirm_delete.html', {'task':task, 'project':project})

def index(request):
    return render(request, 'todo/index.html')
