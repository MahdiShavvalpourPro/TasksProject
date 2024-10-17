# region

import django_filters.rest_framework
from rest_framework import generics, mixins, status
from rest_framework import viewsets
from rest_framework.decorators import api_view

from task_module.models import Task
from .filters import TaskFilter
from .serilizers import TaskSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.urls import reverse


# endregion


# region View Set Api


class TaskViewSetApiView(viewsets.ModelViewSet):
    queryset = Task.objects.order_by('status').all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# endregion


# region TasksMixinApiView

class TasksMixinsFilterApiView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = TaskFilter


# endregion


# region ApiView

# @api_view(['GET'])
# def task_filter(request: Request, status):
#     try:
#         tasks: Task = Task.objects.get(status=status)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# endregion


@api_view(['GET'])
def get_all_tasks(request: Request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return Response(tasks_serializer.data, status=status.HTTP_200_OK)
