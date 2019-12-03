from .models import GlobalConfigModel
from rest_framework import serializers


class GlobalConfigModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalConfigModel
        fields = ['global_config_id',
                  'admin_port',
                  'admin_sport',
                  'admin_ssh_port',
                  'admintimeout',
                  'gui_certificates',
                  'gui_display_hostname',
                  'hostname',
                  'timezone',
                  'config',
                  ]
