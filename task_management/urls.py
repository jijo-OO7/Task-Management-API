# task_management/urls.py (Main Project URLs)
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

"""
Main URL configuration for the task_management project.
Routes all requests to appropriate apps and handles authentication endpoints.
"""

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    
    # Authentication endpoints
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Include task app URLs
    path('api/', include('tasks.urls')),
]
