import django_tables2 as tables

from .models import SNMPSystemConfigModel


class SNMPSystemConfigModelTable(tables.Table):
    description = tables.Column(tables.A('description'), linkify=True)
    status = tables.BooleanColumn(tables.A('Enable SNMP Traps'), yesno='enabled,disabled')
    snmp_system_config_id = tables.LinkColumn('snmp-system-delete', text='Delete', args=[tables.A('pk')],
                                              verbose_name='Delete')

    class Meta:
        model = SNMPSystemConfigModel
        template_name = 'django_tables2/bootstrap.html'
        exclude = ()
        sequence = (
            'description',
            'location',
            'contact',
            'status',
            'config',
            'snmp_system_config_id',
        )
