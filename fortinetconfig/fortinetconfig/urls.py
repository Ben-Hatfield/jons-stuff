"""fortinetconfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView


class HomeView(RedirectView):
    is_permanent = True

    def get_redirect_url(*args, **kwargs):
        return reverse_lazy('config-list')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('templates/', include('apps.templates.urls')),
    path('templates/global/', include('apps.global_config.urls')),
    path('templates/snmp/', include('apps.snmp_config.urls')),
    path('', HomeView.as_view(), name='home')
]
