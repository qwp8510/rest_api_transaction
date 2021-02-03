from fund import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'api/fundTargets', views.TargetsViewSet)
urlpatterns = [
    path('', include(router.urls))
]