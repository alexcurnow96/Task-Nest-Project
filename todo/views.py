# Code taken from Dennis Ivy (see ReadMe for details)

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Task, Project
from .forms import ProjectForm, TaskForm


#-----------------------PROJECTS-------------------------#
class ProjectList(LoginRequiredMixin, ListView):
    model = Project
    template_name = "project_list.html"
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.all()
        return context

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project 
    form_class = ProjectForm 
    template_name = 'project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project 
    form_class = ProjectForm 
    template_name = 'project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project 
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('project_list')

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)






#-----------------------USERS------------------------#
class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super().get(self.request, *args, **kwargs)




#-----------------------TASKS-------------------------#
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input)

        context['search_input'] = search_input

        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'task_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, id=self.kwargs['project_id'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = self.project
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def get_success_url(self):
        return redirect('task-create', project_id=some_project.id)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'task_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.project = self.object.project
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        task_id = self.kwargs.get('pk')
        return get_object_or_404(Task, id=task_id, user=self.request.user)

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.User
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = self.project
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'project_id': self.project.id})


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.project = self.object.project 
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'project_id': self.project.id})


def index(request):
    return render(request, 'todo/index.html')
