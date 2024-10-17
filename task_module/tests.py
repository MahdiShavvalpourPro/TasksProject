from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase

import task_module.models
from task_module.models import Task, User


# region test for tasks
class TasksApiTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='<EMAIL>', password='<PASSWORD>')
        self.client.force_authenticate(user=self.user)

    def test_get_all_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)


class GetTaskApiTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='<EMAIL>',
                                             password='<PASSWORD>')
        self.client.force_authenticate(user=self.user)
        Task.objects.create(title='test_1', description='test_1', status=Task.TaskStatus.PENDING, user=self.user)

    def test_get_task(self):
        url = reverse('task-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), dict)

    def test_get_non_existent_task(self):
        url = reverse('task-detail', kwargs={'pk': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_task_without_authenticated_user(self):
        self.client.logout()
        url = reverse('task-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CreateTaskApiTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user, created = User.objects.get_or_create(
            username='mahdi',
            defaults={'username': 'testuser', 'password': '123'}
        )
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            'title': 'my title ... ',
            'description': 'this is a description',
            'status': Task.TaskStatus.PENDING,
            'user': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.json(), dict)

    def test_create_task_without_authenticated_user(self):
        self.client.force_authenticate(user=None)
        url = reverse('task-list')
        data = {
            'title': 'Unauthenticated Task',
            'description': 'Trying to create a task without authentication',
            'status': Task.TaskStatus.PENDING,
            'user': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_task_missing_required_fields(self):
        url = reverse('task-list')
        data = {
            # 'title': 'Task without title',
            'description': 'This is a description',
            'status': Task.TaskStatus.PENDING,
            'user': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(response.json(), dict)

    def test_create_task_title_too_long(self):
        url = reverse('task-list')
        data = {
            'title': 'T' * 300,
            'description': 'This is a description',
            'status': Task.TaskStatus.PENDING,
            'user': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.json())



    # endregion
