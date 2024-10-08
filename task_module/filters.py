import django_filters

from task_module.models import Task


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=Task.TaskStatus.choices)

    class Meta:
        model = Task
        fields = ['status']
