from django import forms
from django.utils.translation import gettext_lazy as _

from .models import ConfigModel


class ConfigForm(forms.ModelForm):
    class Meta:
        model = ConfigModel
        exclude = ()
        labels = {
            'name': _("Configuration Name"),

        }
        widgets = {
            'name': forms.Textarea(attrs={'cols': 64, 'rows': 1}),
        }
