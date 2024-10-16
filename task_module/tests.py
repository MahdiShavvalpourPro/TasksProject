from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase

from task_module.models import Task, User


# test for get all tasks
class TasksApiTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

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
