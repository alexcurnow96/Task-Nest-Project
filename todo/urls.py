# Code partially taken from Dennis Ivy (see ReadMe for more details)

from django.urls import path
from . import views
from .views import task_list, task_create, task_delete, task_detail, task_update
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', views.index, name='index'),
    path('tasks', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('create-task/', views.task_create, name='task_create'),
    path('task-update/<int:pk>/', views.task_update, name='task_update'),
    path('task-delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/toggle/', views.toggle_task, name='toggle_task'),
]
