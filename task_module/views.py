# region

import django_filters.rest_framework
from rest_framework import generics, mixins
from rest_framework import viewsets

from task_module.models import Task
from .filters import TaskFilter
from .serilizers import TaskSerializer


# endregion


# region View Set Api


class TaskViewSetApiView(viewsets.ModelViewSet):
    queryset = Task.objects.order_by('status').all()
    serializer_class = TaskSerializer


# endregion


# region TasksMixinApiView

class Test(viewsets.GenericViewSet, mixins.ListModelMixin):
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
