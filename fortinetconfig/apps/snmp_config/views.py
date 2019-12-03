import django_tables2 as tables
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from .forms import SNMPSystemConfigForm
from .models import SNMPSystemConfigModel
from .serializers import SNMPSystemConfigModelSerializer
from .tables import SNMPSystemConfigModelTable


# Create your views here.
class SNMPSystemConfigModelViewSet(viewsets.ModelViewSet):
    queryset = SNMPSystemConfigModel.objects.all()
    serializer_class = SNMPSystemConfigModelSerializer
    filterset_fields = SNMPSystemConfigModelSerializer.Meta.fields


class SNMPSystemConfigModelListView(tables.SingleTableView):
    model = SNMPSystemConfigModel
    table_class = SNMPSystemConfigModelTable
    template_name = 'generic/list_view.html'


class SNMPSystemConfigModelCreateView(generic.CreateView):
    queryset = SNMPSystemConfigModel.objects.all()
    template_name = 'generic/form_view.html'
    form_class = SNMPSystemConfigForm
    success_url = reverse_lazy('snmp-system-list')


class SNMPSystemConfigModelDetailView(generic.UpdateView):
    model = SNMPSystemConfigModel
    form_class = SNMPSystemConfigForm
    template_name = 'generic/form_view.html'
    success_url = reverse_lazy('snmp-system-list')


class SNMPSystemConfigModelDeleteView(generic.DeleteView):
    queryset = SNMPSystemConfigModel.objects.all()
    template_name = 'generic/delete_confirmation.html'
    form_class = SNMPSystemConfigForm
    success_url = reverse_lazy('snmp-system-list')


class SNMPSystemConfigModelBasicView(generic.DetailView):
    queryset = SNMPSystemConfigModel.objects.all()
    template_name = 'snmp_config/system_basic_config.html'

    def render_to_response(self, context, **response_kwargs):
        ret = super().render_to_response(context, content_type='text/text', **response_kwargs)
        return ret
