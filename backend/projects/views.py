# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsClientOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsClientOrReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.role == 'client':
            return Project.objects.filter(client=user)
        elif user.role == 'editor':
            return Project.objects.filter(editor=user)
        return Project.objects.none()

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
