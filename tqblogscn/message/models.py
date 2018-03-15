from django.db import models

from db.base import BaseModels



class FreshNews(BaseModels):
    title = models.CharField(max_length=256,verbose_name='新闻标题')
    url = models.URLField(verbose_name='新闻链接')
    views = models.CharField(max_length=12, verbose_name='新鲜度')
    category = models.CharField(max_length=24, verbose_name='来源')

    class Meta:
        verbose_name = '新鲜事'
        verbose_name_plural = verbose_name
        ordering = ['-views']

    def __str__(self):
        return self.title


class BlogsRecord(BaseModels):
    title = models.CharField(max_length=50,verbose_name='博客标题')
    url = models.URLField(verbose_name='博客链接')
    images = models.ImageField(upload_to='images/message/', verbose_name='博客图片')
    abstract = models.TextField(verbose_name='博客简介')

    class Meta:
        verbose_name = '博客收录'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.title


