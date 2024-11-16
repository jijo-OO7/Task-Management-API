from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.
    Handles validation and data transformation.
    """
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 
                 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        """Validate that title is not empty"""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value
