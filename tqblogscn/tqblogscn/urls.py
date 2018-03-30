
import xadmin
from xadmin.plugins import xversion
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from blogs import views

xadmin.autodiscover()
xversion.register_models()

urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^', include('blogs.urls', namespace='blogs')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r'^search/', include('haystack.urls', namespace='haystack')),
    url(r'^ueditor/', include('DjangoUeditor.urls', namespace='ueditor')),
    url(r'^movies/',include('movies.urls', namespace='movies')),
    url(r'^message/',include('message.urls', namespace='message')),
    url(r'^study/', include('study.urls', namespace='study')),
    url(r'^api/', include('api.urls', namespace='api')),
]

handler404 = views.page_not_found
handler500 = views.page_error


from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


