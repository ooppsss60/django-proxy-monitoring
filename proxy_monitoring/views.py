from django.contrib.auth.mixins import UserPassesTestMixin
from revproxy.views import ProxyView

from proxy_monitoring import config


class BaseProxyView(UserPassesTestMixin, ProxyView):
    def test_func(self):
        return self.request.user.is_superuser


class FlowerView(BaseProxyView):
    upstream = config.FLOWER_UPSTREAM

    def dispatch(self, request, path):
        response = super(FlowerView, self).dispatch(request, path)
        content_type = response.headers.get('Content-Type')
        if content_type and 'html' in content_type:
            response.content = response.content.decode().replace(
                '="/', '="/monitoring/flower/'
            ).encode()
        return response


class GrafanaView(BaseProxyView):
    upstream = config.GRAFANA_UPSTREAM

    def dispatch(self, request, path):
        response = super(GrafanaView, self).dispatch(request, path)
        content_type = response.headers.get('Content-Type')
        if content_type and 'html' in content_type:
            response.content = response.content.decode().replace(
                '="/', '="/monitoring/grafana/'
            ).encode()
        return response