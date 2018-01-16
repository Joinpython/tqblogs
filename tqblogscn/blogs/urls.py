from django.conf.urls import url
from blogs import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^detail/(\d+)/', views.detail, name='detail'),
    url(r'^list/(\d+)/', views.list, name='list'),
    url(r'^article/(\d+)', views.article, name='article'),
    url(r'^messageboard/', views.messageboard, name='messageboard'),
]
