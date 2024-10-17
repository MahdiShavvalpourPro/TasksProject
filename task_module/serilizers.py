from rest_framework import serializers
from task_module.models import Task, User


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Task
        fields = '__all__'
        # fields = ['id', 'title', 'description', 'user', 'created_at', 'updated_at', 'status']

    # def create(self, validated_data):
    #     user = validated_data.pop('user')
    #     task = Task.objects.create(**validated_data)
    #     return task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
