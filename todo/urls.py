# Code partially taken from Dennis Ivy (see ReadMe for more details)

from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', views.index, name='index'),
    path('tasks', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/<int:project_id>/task/', TaskCreate.as_view(), name='task-create'),
    path('create-task/', TaskCreate.as_view(), name='task-create-no-project'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),


    path('project', views.project_list, name='project_list'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/new', views.create_project, name='create_project'),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('project/<int:project_id>/edit/', views.edit_project, name='edit_project'),
    
]