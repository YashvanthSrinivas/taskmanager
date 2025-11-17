from django.shortcuts import render
from rest_framework import generics, permissions

from tasks.models import Task
from tasks.serializers import TaskSerializer

# List tasks and create new tasks
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Superuser sees all tasks
        if user.is_superuser:
            return Task.objects.all()

        # Normal users see only their tasks
        return Task.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Retrieve, update, delete a single task
class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Task.objects.all()

        return Task.objects.filter(user=user)
