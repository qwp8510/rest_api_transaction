from receivers import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'api/receivers', views.ReceiversViewSet)
urlpatterns = [
    path('', include(router.urls))
]
