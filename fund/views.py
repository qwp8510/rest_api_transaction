from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from fund.models import Targets
from fund.serializers import TargetsSerializer

class TargetsViewSet(viewsets.ModelViewSet):
    queryset = Targets.objects.all()
    serializer_class = TargetsSerializer
