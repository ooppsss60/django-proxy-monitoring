from django.conf import settings

GRAFANA_UPSTREAM = settings.GRAFANA_URL if hasattr(settings, 'GRAFANA_URL') else None
FLOWER_UPSTREAM = settings.FLOWER_URL if hasattr(settings, 'FLOWER_URL') else None