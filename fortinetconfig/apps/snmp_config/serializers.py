from .models import SNMPSystemConfigModel
from rest_framework import serializers


class SNMPSystemConfigModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SNMPSystemConfigModel
        fields = ['snmp_system_config_id',
                  'contact',
                  'description',
                  'location',
                  'status',
                  'config',
                  ]
