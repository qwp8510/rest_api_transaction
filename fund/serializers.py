from rest_framework import serializers
from fund.models import Targets


class TargetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Targets
        fields = ('id', 'name', 'currency', 'fundType', 'company', 'partition', 'dividendFrequency',
                  'url', 'code')
