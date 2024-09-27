from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Project
from todo.models import Task
from .forms import ProjectForm


#-----------------------PROJECTS-------------------------#
@login_required
def project_list(request):
    project_list = Project.objects.filter(user=request.user)
    context = {
        'project_list': project_list,  
    }
    return render(request, 'projects/project_list.html', context)

@login_required
def project_detail(request, pk):
    task = get_object_or_404(Project, pk=pk, user=request.user)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def project_create(request):
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_form.html', {'form': form})

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'projects/project_form.html', {'form': form})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    
    return render(request, 'projects/confirm_delete.html', {'object': project})
