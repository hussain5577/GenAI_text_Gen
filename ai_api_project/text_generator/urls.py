from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TextGenerationViewSet

router = DefaultRouter()
router.register(r'generations', TextGenerationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]