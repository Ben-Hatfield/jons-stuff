from .models import ConfigModel
from rest_framework import serializers


class ConfigModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigModel
        fields = [
                  'name',
                  ]
