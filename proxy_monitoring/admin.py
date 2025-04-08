from django.contrib import admin
from django.shortcuts import redirect

from proxy_monitoring import config
from proxy_monitoring.models import Flower, Grafana


class MonitoringAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj = ...):
        return False

    def has_add_permission(self, request):
        return False


class FlowerAdmin(MonitoringAdmin):
    def changelist_view(self, request, *args, **kwargs):
        return redirect('flower-proxy', path='')


class GrafanaAdmin(MonitoringAdmin):
    def changelist_view(self, request, *args, **kwargs):
        return redirect('grafana-proxy', path='')


if config.FLOWER_UPSTREAM:
    admin.site.register(Flower, FlowerAdmin)

if config.GRAFANA_UPSTREAM:
    admin.site.register(Grafana, GrafanaAdmin)