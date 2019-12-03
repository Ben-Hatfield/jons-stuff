from django.db import models
from django.shortcuts import reverse


class ConfigModel(models.Model):
    configuration_id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    def get_absolute_url(self):
        return reverse('config-detail', args=(self.pk,))

    def get_delete_url(self):
        return reverse('config-delete', args=(self.pk,))

    def __str__(self):
        return '{}'.format(self.name)
