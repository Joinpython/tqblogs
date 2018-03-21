
from django.conf.urls import url
from api import views


urlpatterns = [
    url(r'^index/', views.IndexView.as_view(), name='index'),
    url(r'^fresh/', views.FreshView.as_view(), name='fresh'),
    url(r'^collection/', views.BlogsRecordView.as_view(), name='collection'),
    url(r'^movies/', views.MoviesView.as_view(), name='movies'),
    url(r'^watch/', views.WatchMoviesView.as_view(), name='watch'),
    url(r'^study/', views.StudyView.as_view(), name='study'),
    url(r'^look/', views.ArticleLookView.as_view(), name='look'),
]