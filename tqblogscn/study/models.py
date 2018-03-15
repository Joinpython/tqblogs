from django.db import models
from db.base import BaseModels

class Study(BaseModels):
    title = models.CharField(max_length=56, verbose_name='资源标题')
    url = models.URLField(verbose_name='资源链接')
    password = models.CharField(default='0000',max_length=24,verbose_name='链接密码')
    abstract = models.TextField(verbose_name='资源简介')
    images = models.ImageField(upload_to='study/images/', verbose_name='资源图片')

    class Meta:
        verbose_name = '资源'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.title


