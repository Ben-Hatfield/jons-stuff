from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('global', GlobalConfigModelViewSet)

urlpatterns = [
    path('list', GlobalConfigModelListView.as_view(), name='global-list'),
    path('create/', GlobalConfigModelCreateView.as_view(), name='global-create'),
    path('<int:pk>/', GlobalConfigModelDetailView.as_view(), name='global-detail'),
    path('<int:pk>/basic', GlobalConfigModelBasicView.as_view(), name='global-basic'),
    path('<int:pk>/delete', GlobalConfigModelDeleteView.as_view(), name='global-delete'),
    path('', include(router.urls)),
]
