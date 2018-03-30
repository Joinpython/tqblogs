from  django.conf.urls import url
from message import views


urlpatterns = [
    url(r'^fresh/$',views.fresh_news, name='fresh_news'),
    url(r'^collect/$',views.collect, name='collect'),
]