from django.conf.urls import url
from blogs import views, views_item


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/', views.detail, name='detail'),
    url(r'^list/(\d+)/', views.list, name='list'),
    url(r'^article/(\d+)/', views.article, name='article'),
    url(r'^messageboard/', views.messageboard, name='messageboard'),
    url(r'api-index/', views_item.index_item,name='index_item'),
    url(r'api-comment/', views_item.comment_item,name='comment_item')
]
