from django.shortcuts import render
from rest_framework import viewsets
from task_module.models import Task
from .serilizers import TaskSerializer


# Create your views here.


# region View Set Api

class TaskViewSetApiView(viewsets.ModelViewSet):
    queryset = Task.objects.order_by('status').all()
    serializer_class = TaskSerializer


# endregion
