from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from .serializers import CustomUserSerializer
from .permissions import IsUser


class Dashboard(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsUser]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user
