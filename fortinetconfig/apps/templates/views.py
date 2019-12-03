import django_tables2 as tables
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
from .forms import ConfigForm
from .models import ConfigModel
from .serializers import ConfigModelSerializer
from .tables import ConfigModelTable


# Create your views here.
class ConfigModelViewSet(viewsets.ModelViewSet):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigModelSerializer
    filterset_fields = ConfigModelSerializer.Meta.fields


class ConfigModelListView(tables.SingleTableView):
    model = ConfigModel
    table_class = ConfigModelTable
    template_name = 'generic/list_view.html'


class ConfigModelCreateView(generic.CreateView):
    queryset = ConfigModel.objects.all()
    template_name = 'generic/form_view.html'
    form_class = ConfigForm
    success_url = reverse_lazy('config-list')


class ConfigModelDetailView(generic.UpdateView):
    model = ConfigModel
    form_class = ConfigForm
    template_name = 'generic/form_view.html'
    success_url = reverse_lazy('config-list')


class ConfigModelDeleteView(generic.DeleteView):
    queryset = ConfigModel.objects.all()
    template_name = 'generic/delete_confirmation.html'
    form_class = ConfigForm
    success_url = reverse_lazy('config-list')


class ConfigModelBasicView(generic.DetailView):
    queryset = ConfigModel.objects.all()
    template_name = 'templates/basic_config.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['global_config'] = context['configmodel'].globalconfigmodel
        except ObjectDoesNotExist:
            pass
        try:
            context['snmp_system_config'] = context['configmodel'].snmpsystemconfigmodel
        except ObjectDoesNotExist:
            pass

        return context

    def render_to_response(self, context, **response_kwargs):
        ret = super().render_to_response(context, content_type='text/text', **response_kwargs)
        return ret
