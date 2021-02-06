from rest_framework import viewsets
from rest_framework import permissions

from receivers.models import Receivers
from receivers.serializers import ReceiversSerializer


class ReceiversViewSet(viewsets.ModelViewSet):
    queryset = Receivers.objects.all()
    serializer_class = ReceiversSerializer
    permission_classes = [permissions.DjangoModelPermissions]
