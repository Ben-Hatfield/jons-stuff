from django.db import models
from django.shortcuts import reverse
from apps.fortinet_globals import time_zone_choices
from apps.templates.models import ConfigModel


class GlobalConfigModel(models.Model):
    global_config_id = models.BigAutoField(primary_key=True)
    hostname = models.TextField()
    admin_port = models.IntegerField(default=80, blank=True, null=True)
    admin_sport = models.IntegerField(default=443, blank=True, null=True)
    admin_ssh_port = models.IntegerField(default=22, blank=True, null=True)
    admintimeout = models.IntegerField(default=30, blank=True, null=True)
    gui_certificates = models.NullBooleanField(default=False)
    gui_display_hostname = models.NullBooleanField(default=False)
    timezone = models.TextField(blank=True, null=True, default='08', choices=time_zone_choices)
    config = models.OneToOneField(ConfigModel, blank=True, null=True, on_delete='SET_NULL')

    def get_absolute_url(self):
        return reverse('global-detail', args=(self.pk,))

    def get_delete_url(self):
        return reverse('global-delete', args=(self.pk,))
