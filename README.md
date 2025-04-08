# django-proxy-monitoring

Flower & Grafana monitoring in Django Admin

### Installation

```
pip install django-revproxy
pip install git+ssh://github.com/ooppsss60/django-proxy-monitoring.git
```
Update settings
```
INSTALLED_APPS = [
    ...
    "revproxy.apps.RevProxyConfig",
    "proxy_monitoring.apps.ProxyMonitoringConfig",
    ...
]

FLOWER_URL = os.environ.get("FLOWER_URL", "")
GRAFANA_URL = os.environ.get("GRAFANA_URL", "")
```
Register urls
```
urlpatterns = [
    ...
    path("monitoring/", include("proxy_monitoring.urls")),
    ...
]
```
