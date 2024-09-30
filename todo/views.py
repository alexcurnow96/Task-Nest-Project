# Code taken from Dennis Ivy (see ReadMe for details)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
from .models import Task
from django.db.models import Q
from .forms import TaskForm

from django.http import JsonResponse
from django.views.decorators.http import require_POST



#-----------------------TASKS-------------------------#
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    count = tasks.filter(completed=False).count()

    context = {
        'tasks': tasks,
        'count': count,
    }
    return render(request, 'todo/task_list.html', context)

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, 'todo/task.html', {'task': task})

def task_create(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'todo/task_form.html', {'form': form})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    context = {'form': form}
    return render(request, 'todo/task_form.html', context)

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'todo/task_confirm_delete.html', {'task':task})

def index(request):
    return render(request, 'todo/index.html')



# TOGGLE TASK FOR CHECKLIST

@login_required
@require_POST
def toggle_task(request, task_id):
    task = Task.objects.get(id=task.id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'status':'success', 'completed': task.completed})