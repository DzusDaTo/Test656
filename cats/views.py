from .models import Cat
from .serializers import CatSerializer
from rest_framework import viewsets, permissions
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer


class CatViewSet(viewsets.ModelViewSet):
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cat.objects.all()

    def get_queryset(self):
        # Возвращаем только котов, принадлежащих текущему пользователю
        return Cat.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Устанавливаем текущего пользователя как владельца кота
        serializer.save(user=self.request.user)


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]