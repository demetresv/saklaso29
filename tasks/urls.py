from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListView.as_view(), ),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), ),
    path('tags/', views.TagListView.as_view(), ),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), ),
]
