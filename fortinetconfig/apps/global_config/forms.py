from django import forms
from django.utils.translation import gettext_lazy as _

from .models import GlobalConfigModel


class GlobalConfigForm(forms.ModelForm):
    class Meta:
        model = GlobalConfigModel
        exclude = ()
        labels = {
            'hostname': _("Unit's hostname."),
            'admin_port': _("HTTP Admin Port"),
            'admin_sport': _("HTTPS Admin Port"),
            'admin_ssh_port': _("SSH Admin Port"),
            'admintimeout': _("Administrative Session Timeout"),
            'gui_certificates': _("Enable/disable Certificate GUI page"),
            'gui_display_hostname': _("Enable/disable hostname display on login page"),
            'timezone': _("Set Timezone"),
        }
        help_texts = {
            'hostname': _("Most models will truncate names longer than 24 characters."
                          " Some models support hostnames up to 35 characters."),
            'admintimeout': _("Number of minutes before an idle administrator session times out"
                              "(5 - 480 minutes (8 hours), default = 5)."),
            'gui_certificates': _("Allows adding and configuring certificates from the GUI."),
        }
        widgets = {
            'hostname': forms.Textarea(attrs={'cols': 35, 'rows': 1}),
        }
