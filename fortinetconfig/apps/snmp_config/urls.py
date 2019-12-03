from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('api', SNMPSystemConfigModelViewSet)

urlpatterns = [
    path('', SNMPSystemConfigModelListView.as_view(), name='snmp-system-list'),
    path('create/', SNMPSystemConfigModelCreateView.as_view(), name='snmp-system-create'),
    path('<int:pk>/', SNMPSystemConfigModelDetailView.as_view(), name='snmp-system-detail'),
    path('<int:pk>/basic', SNMPSystemConfigModelBasicView.as_view(), name='snmp-system-basic'),
    path('<int:pk>/delete', SNMPSystemConfigModelDeleteView.as_view(), name='snmp-system-delete'),
    path('', include(router.urls)),
]
