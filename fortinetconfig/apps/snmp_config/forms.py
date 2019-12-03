from django import forms
from django.utils.translation import gettext_lazy as _

from .models import SNMPSystemConfigModel


class SNMPSystemConfigForm(forms.ModelForm):
    class Meta:
        model = SNMPSystemConfigModel
        exclude = ()
        labels = {
            'contact': _("Contact information"),
            'description': _("Description"),
            'location': _("Physical Location"),
            'status': _("Enable/disable the SNMP agent"),
        }
        help_texts = {
            'status': _("If enabled, system can send traps and receive queries."),
        }

