from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'cats', CatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]