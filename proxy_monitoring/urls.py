from django.urls import re_path

from proxy_monitoring import config
from proxy_monitoring.views import FlowerView, GrafanaView


urlpatterns = []

if config.FLOWER_UPSTREAM:
    urlpatterns.append(re_path(r'flower/(?P<path>.*)', FlowerView.as_view(), name='flower-proxy'))

if config.GRAFANA_UPSTREAM:
    urlpatterns.append(re_path(r'grafana/(?P<path>.*)', GrafanaView.as_view(), name='grafana-proxy'))