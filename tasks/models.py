from django.contrib.auth.models import User
from django.db import models



class Task(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Assign a task to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='tasks')

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title
