
import xadmin
from xadmin.plugins import xversion
from django.conf.urls import url, include
from django.views.generic.base import RedirectView


xadmin.autodiscover()
xversion.register_models()

urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    url(r'^search/', include('haystack.urls', namespace='haystack')),
    url(r'^ueditor/', include('DjangoUeditor.urls', namespace='ueditor')),
    url(r'^blogs/', include('blogs.urls', namespace='blogs')),
]
