import django_tables2 as tables

from .models import GlobalConfigModel


class GlobalConfigModelTable(tables.Table):
    hostname = tables.Column(tables.A('Hostname'), linkify=True)
    gui_certificates = tables.BooleanColumn(tables.A('Show GUI Certificates'), yesno='enabled,disabled')
    gui_display_hostname = tables.BooleanColumn(tables.A('Show Hostname'), yesno='enabled,disabled')
    global_config_id = tables.LinkColumn('global-delete', text='Delete', args=[tables.A('pk')], verbose_name='Delete')

    class Meta:
        model = GlobalConfigModel
        template_name = 'django_tables2/bootstrap.html'
        exclude = (
            [
                # ' field_name'
            ]
        )
        sequence = (
            'hostname',
            'admin_port',
            'admin_sport',
            'admin_ssh_port',
            'admintimeout',
            'gui_certificates',
            'gui_display_hostname',
            'timezone',
            'config',
            'global_config_id',
        )
