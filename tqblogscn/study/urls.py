from django.conf.urls import url

from study import views


urlpatterns = [
    url(r'^download/$', views.download, name='download'),
]