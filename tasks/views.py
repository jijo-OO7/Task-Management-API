from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    
    #API view to create a new task or list all tasks.
    #Requires authentication.
    
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return only tasks belonging to the current user"""
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Save the task with the current user"""
        serializer.save(user=self.request.user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    
    #API view to retrieve, update or delete a specific task.
    #Requires authentication and ownership of the task.

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        #Return only tasks belonging to the current user
        return Task.objects.filter(user=self.request.user)

class TaskCompleteView(APIView):
    
    #API view to mark a task as complete.
    #Requires authentication and ownership of the task.
    
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
            task.status = 'completed'
            task.save()
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(
                {"error": "Task not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
