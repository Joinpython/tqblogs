from django.conf.urls import url
from blogs import views, views_item


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(\d+)/', views.detail, name='detail'),
    url(r'^lists/(\d+)/', views.list, name='list'),
    url(r'^articles/(\d+)/', views.article, name='article'),
    url(r'^categorys/(\d+)/', views.categorys, name='categorys'),
    url(r'^messageboard/', views.messageboard, name='messageboard'),
    url(r'api-index/', views_item.index_item,name='index_item'),
    url(r'api-comment/', views_item.comment_item,name='comment_item'),
    url(r'^resume/', views.resume, name='resume'),
]
