from django.urls import path

urlpatterns = [
    path('tasks/', views.TaskListView.as_view),
    path('tasks/<int: pk>', views.TaskDetailView.as_view),
    path('tags/', views.TagListView.as_view),
    path('tags/<int:pk>', views.TaskDetailView.as_view),
]
