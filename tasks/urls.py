from django.urls import path
from .views import (
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
    TaskCompleteView
)

"""
URL configuration for the tasks app.
Handles all task-related endpoints.
"""

urlpatterns = [
    # Task CRUD operations
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', TaskCompleteView.as_view(), name='task-complete'),
]
