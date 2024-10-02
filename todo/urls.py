# Code partially taken from Dennis Ivy (see ReadMe for more details)

from django.urls import path, include
from . import views
from .views import task_list, task_create, task_delete, task_detail, task_update
from django.contrib.auth.views import LogoutView
from tasknest import urls

urlpatterns = [
    #home page
    path('', views.index, name='index'),

    #list all tasks
    path('tasks', views.task_list, name='task_list'),

    #view details of a specific task
    path('task/<int:pk>/', views.task_detail, name='task_detail'),

    #create a new task
    path('create-task/', views.task_create, name='task_create'),

    #update an existing task
    path('task-update/<int:pk>/', views.task_update, name='task_update'),

    #delete a task
    path('task-delete/<int:pk>/', views.task_delete, name='task_delete'),

    #toggle task completion status
    path('toggle-task/<int:task_id>', views.toggle_task, name='toggle_task'),

    #add a comment to a task
    path('task/<int:pk>/comment/', views.add_comment_to_task,
         name='add_comment_to_task'),

    #delete a comment
    path('comment/<int:comment_pk>/delete/',
         views.delete_comment, name='delete_comment'),
]
