from django.conf.urls import url

from movies import views


urlpatterns = [
    url(r'^hot/$', views.hot_movies, name='hot_movies'),
    url(r'^watch/$', views.watch_movies_website, name='watch_movies'),
]