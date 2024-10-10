import graphene
from graphene_django.types import DjangoObjectType
from .models import Task, User


class StatusEnum(graphene.Enum):
    PENDING = "PE"
    IN_PROGRESS = "IN"
    COMPLETED = "CO"


class TaskModelType(DjangoObjectType):
    class Meta:
        model = Task
        fields = '__all__'


class UserModelType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskModelType)

    def resolve_tasks(self, info, **kwargs):
        return Task.objects.all()


schema = graphene.Schema(query=Query)
