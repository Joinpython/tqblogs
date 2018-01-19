
import xadmin
from xadmin.plugins import xversion
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from rest_framework import routers
from blogs import views

xadmin.autodiscover()
xversion.register_models()

# router = routers.DefaultRouter()
# router.register(r'article', views.ArticleViewSet)
# router.register(r'comment', views.CommentViewSet)

urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    url(r'^search/', include('haystack.urls', namespace='haystack')),
    url(r'^ueditor/', include('DjangoUeditor.urls', namespace='ueditor')),
    url(r'^blogs/', include('blogs.urls', namespace='blogs')),
    # url(r'api/',include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api-article/', include(router.urls))
]
