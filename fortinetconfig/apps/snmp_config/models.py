from django.db import models
from django.shortcuts import reverse

from apps.templates.models import ConfigModel


class SNMPSystemConfigModel(models.Model):
    snmp_system_config_id = models.BigAutoField(primary_key=True)
    contact = models.CharField(max_length=35, blank=True, null=True)
    description = models.CharField(max_length=35, blank=True, null=True)
    location = models.CharField(max_length=35, blank=True, null=True)
    status = models.NullBooleanField(default=False)
    config = models.OneToOneField(ConfigModel, blank=True, null=True, on_delete='SET_NULL')

    def get_absolute_url(self):
        return reverse('snmp-system-detail', args=(self.pk,))

    def get_delete_url(self):
        return reverse('snmp-system-delete', args=(self.pk,))

    def __str__(self):
        return '{}:{}:{}:{}abled->{}'.format(self.description,
                                             self.location,
                                             self.contact,
                                             'En' if self.status else 'Dis',
                                             self.config
                                             )
