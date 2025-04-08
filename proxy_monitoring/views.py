from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from revproxy.views import ProxyView

from proxy_monitoring import config


class BaseProxyView(UserPassesTestMixin, ProxyView):
    def test_func(self):
        return self.request.user.is_superuser


class FlowerView(BaseProxyView):
    upstream = config.FLOWER_UPSTREAM

    def dispatch(self, request, path):
        response: HttpResponse = super(FlowerView, self).dispatch(request, path)
        content_type = response.headers.get('Content-Type')
        if content_type and 'html' in content_type:
            content = response.content.decode().replace(
                '="/', '="/monitoring/flower/'
            ).encode()
            response = HttpResponse(
                content,
                content_type=content_type,
                status=response.status_code
            )
        return response


class GrafanaView(BaseProxyView):
    upstream = config.GRAFANA_UPSTREAM

    def dispatch(self, request, path):
        response = super(GrafanaView, self).dispatch(request, path)
        content_type = response.headers.get('Content-Type')
        if content_type and 'html' in content_type:
            content = response.content.decode().replace(
                '="/', '="/monitoring/grafana/'
            ).encode()
            response = HttpResponse(
                content,
                content_type=content_type,
                status=response.status_code
            )
        return response