from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CalculatorViewSet

router = DefaultRouter()
router.register('calculator', CalculatorViewSet, basename='calculator')

urlpatterns = [
    path('', include(router.urls)),
]
