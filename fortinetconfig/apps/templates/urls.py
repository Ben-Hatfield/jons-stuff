from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('api', ConfigModelViewSet)

urlpatterns = [
    path('', ConfigModelListView.as_view(), name='config-list'),
    path('create/', ConfigModelCreateView.as_view(), name='config-create'),
    path('<int:pk>/', ConfigModelDetailView.as_view(), name='config-detail'),
    path('<int:pk>/basic', ConfigModelBasicView.as_view(), name='config-basic'),
    path('<int:pk>/delete', ConfigModelDeleteView.as_view(), name='config-delete'),
    path('', include(router.urls)),
]
