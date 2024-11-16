import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tasks.models import Task
from django.utils import timezone
from datetime import date

@pytest.mark.django_db
class TestTaskAPI:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    @pytest.fixture
    def authenticated_client(self, api_client, user):
        api_client.force_authenticate(user=user)
        return api_client

    def test_create_task(self, authenticated_client, user):
        task_data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'due_date': date.today(),
        }
        
        response = authenticated_client.post('/api/tasks/', task_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Task.objects.count() == 1
        assert Task.objects.first().user == user

    def test_complete_task(self, authenticated_client, user):
        task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date=date.today(),
            user=user
        )
        
        response = authenticated_client.patch(
            f'/api/tasks/{task.id}/complete/'
        )
        assert response.status_code == status.HTTP_200_OK
        assert Task.objects.first().status == 'completed'
