from rest_framework import serializers
from receivers.models import Receivers


class ReceiversSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receivers
        fields = ('id', 'name', 'targets', 'receiveFrequency', 'lineToken')
