# Code partially taken from Dennis Ivy (see ReadMe for more details)

from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, ProjectList, ProjectDetail, ProjectCreate, ProjectDelete, ProjectUpdate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', views.index, name='index'),
    path('tasks', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('create-task/<int:project_id>/task/', TaskCreate.as_view(), name='task_create'),
    path('create-task/', TaskCreate.as_view(), name='task_create_no_project'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),


    path('project', ProjectList.as_view(), name='project_list'),
    path('project/<int:project_id>/', ProjectDetail.as_view(), name='project_detail'),
    path('project/new', ProjectCreate.as_view(), name='project_create'),
    path('project/<int:project_id>/delete/', ProjectDelete.as_view(), name='project_delete'),
    path('project/<int:project_id>/edit/', ProjectUpdate.as_view(), name='project_update'),
    
]