from django.urls import path
from . import views
from .views import task_list, task_create, task_delete, task_detail, task_update
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('project', views.project_list, name='project_list'),
  path('project/<int:pk>/', niews.project_detail, name='project_detail'),
  path('project/create/', views.project_create, name='project_create'),
  path('project/<int:pk>/update/', views.project_update, name='project_update'),
  path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
]