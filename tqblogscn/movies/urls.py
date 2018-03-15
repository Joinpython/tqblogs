from django.conf.urls import url

from movies import views


urlpatterns = [
    url(r'^hot/', views.hot_movies, name='hot_movies'),
    url(r'^top/', views.top_movies, name='top_movies'),
    url(r'^original/', views.original_movies, name='original_movies'),
    url(r'^watch_movies/', views.watch_movies_website, name='watch_movies'),
]