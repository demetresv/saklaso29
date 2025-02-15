from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer
from rest_framework import generics


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        if self.request.query_params.get('orderby'):
            super().get_queryset().order_by(self.request.query_params.get('orderby'))
        else:
            return super().get_queryset()

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['assigned_to'] = 'Unknown'
        return super().create(request, *args, **kwargs)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_destroy(self, instance):
        instance.archived = True
        instance.save()


class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer