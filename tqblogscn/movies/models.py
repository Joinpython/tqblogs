from django.db import models
from db.base import BaseModels


class Movies(BaseModels):
    title = models.CharField(max_length=56, verbose_name='电影标题')
    url = models.URLField(verbose_name='电影链接')
    rate = models.CharField(max_length=10, verbose_name='电影评分')
    images = models.ImageField(upload_to='movies/images/', verbose_name='电影图片')
    abstract = models.TextField(verbose_name='电影简介')

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = verbose_name
        ordering = ['-rate']

    def __str__(self):
        return self.title


class WatchMovies(BaseModels):
    title = models.CharField(max_length=50, verbose_name='网站名')
    url = models.URLField(verbose_name='网站地址')
    abstract = models.TextField(verbose_name='网站简介')
    images = models.ImageField(upload_to='movies/website_images/', verbose_name='网站图片')

    class Meta:
        verbose_name = '观影小站'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.title

