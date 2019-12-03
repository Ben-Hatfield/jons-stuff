import django_tables2 as tables

from .models import ConfigModel


class ConfigModelTable(tables.Table):
    name = tables.Column(tables.A('Config Name'), linkify=True)
    basic = tables.TemplateColumn('<a href="{% url \'config-basic\' pk=record.pk %}">Basic Configuration</a>',
                                  verbose_name='Basic Configuration')
    configuration_id = tables.LinkColumn('config-delete', text='Delete', args=[tables.A('pk')], verbose_name='Delete')

    class Meta:
        model = ConfigModel
        template_name = 'django_tables2/bootstrap.html'
        exclude = ()
        sequence = ('name', 'basic', 'configuration_id')
