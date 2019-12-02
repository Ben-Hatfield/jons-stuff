from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from .forms import GlobalConfigForm
from .models import GlobalConfigModel
from .serializers import GlobalConfigModelSerializer


# Create your views here.
class GlobalConfigModelViewSet(viewsets.ModelViewSet):
    queryset = GlobalConfigModel.objects.all()
    serializer_class = GlobalConfigModelSerializer
    filterset_fields = GlobalConfigModelSerializer.Meta.fields


class GlobalConfigModelListView(generic.ListView):
    queryset = GlobalConfigModel.objects.all()
    template_name = 'global_config/list_view.html'


class GlobalConfigModelCreateView(generic.CreateView):
    queryset = GlobalConfigModel.objects.all()
    template_name = 'generic/form_view.html'
    form_class = GlobalConfigForm
    success_url = reverse_lazy('global-list')


class GlobalConfigModelDetailView(generic.UpdateView):
    model = GlobalConfigModel
    form_class = GlobalConfigForm
    template_name = 'generic/form_view.html'
    success_url = reverse_lazy('global-list')


class GlobalConfigModelDeleteView(generic.DeleteView):
    queryset = GlobalConfigModel.objects.all()
    template_name = 'generic/delete_confirmation.html'
    form_class = GlobalConfigForm
    success_url = reverse_lazy('global-list')


class GlobalConfigModelBasicView(generic.DetailView):
    queryset = GlobalConfigModel.objects.all()
    template_name = 'global_config/basic_config.html'

    def render_to_response(self, context, **response_kwargs):
        ret = super().render_to_response(context, content_type='text/text', **response_kwargs)
        return ret

