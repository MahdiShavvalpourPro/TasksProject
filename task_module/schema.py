import graphene
from graphene_django.types import DjangoObjectType
from .models import Task


class TaskModelType(DjangoObjectType):
    class Meta:
        model = Task


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskModelType)

    def resolve_tasks(self, info, **kwargs):
        return Task.objects.all()


schema = graphene.Schema(query=Query)
