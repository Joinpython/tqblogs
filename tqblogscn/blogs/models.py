from django.db import models
from db.base import BaseModels
from utils.enums import *
from datetime import datetime
from DjangoUeditor.models import UEditorField


# 分类
class Category(models.Model):
    categor = models.CharField(max_length=56, verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.categor


# 友情链接(links)模型
class Links(models.Model):
    title = models.CharField(max_length=256, verbose_name='标题')
    description = models.CharField(max_length=256, verbose_name='描述')
    callback_url = models.URLField(verbose_name='链接地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.title

# 博客管理
class ArticleManager(models.Manager):
    '''文章模型类管理器'''

    def get_article_by_type(self, type_id,limit=None):
        '''根据文章id查询文章信息'''
        # 查询数据
        order_by = ('type_id',)

        article_list = self.filter(type_id=type_id).order_by(*order_by)

        if limit:
            article_list = article_list[:limit]

        return article_list

    def get_article_by_category(self, category_id, limit=None):
        order_by = ('category_id',)

        article_list = self.filter(category_id=category_id).order_by(*order_by)

        if limit:
            article_list = article_list[:limit]

        return article_list

    #根据创建时间来查询文章
    def get_article_by_create_time(self,limit=None, sort='default'):
        if sort == 'new':
            order_by = ('-create_time',)

        else:
            order_by = ('-pk',)

        article_list = self.filter().order_by(*order_by)

        if limit:
            article_list = article_list[:limit]

        return article_list

    # 根据文章id获取文章信息
    def get_article_by_id(self, article_id):
        try:
            article_list = self.get(id=article_id)

        except self.model.DoesNotExist:
            article_list = None

        return article_list


# 博客
class Article(BaseModels):

    article_id_choices = ((k, v) for k, v in ARTICLE_TYPE.items())
    type_id = models.SmallIntegerField(default=PYTHON, choices=article_id_choices, verbose_name='id')
    type = models.CharField(default='python', choices=article_id_choices, verbose_name='博文类型',max_length=40)
    title = models.CharField(max_length=40, verbose_name='博文标题')
    author = models.CharField(default='漂泊在北京', max_length=20, verbose_name='博文作者')
    count = models.PositiveIntegerField(default=0, verbose_name='浏览量')
    date = models.DateField(verbose_name='发布时间')
    images = models.ImageField(upload_to='images/', verbose_name='博文图片')
    description = models.TextField(verbose_name='博文简介')
    content = UEditorField(width=800, height=600,imagePath='upload/images/', filePath='upload/files/', verbose_name='博文内容')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='标签')

    def views_count(self):
        self.count += 1
        self.save(update_fields=['count'])

    objects = ArticleManager()

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

        ordering = ['create_time']

    def __str__(self):
        return self.title


class CommentManager(models.Manager):

    def create_comment(self,author, email, comment,blogs_id,url=None):

        cont = self.create(name=author,email=email,url=url,
                           comment=comment,blogs_id=blogs_id,
                           number=0,blogs=None,)

        return cont


# 评论
class Comment(BaseModels):
    name = models.CharField(max_length=20,verbose_name='评论人昵称')
    email = models.EmailField(verbose_name='评论人邮件')
    url = models.CharField(max_length=256,verbose_name='网址')
    comment = models.TextField(verbose_name='评论内容')
    blogs = models.ForeignKey(Article, verbose_name='博客')
    number = models.PositiveIntegerField(default=0,verbose_name='评论数')

    objects = CommentManager()

    def views_number(self):
        self.number += 1
        self.save(update_fields=['number'])

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['create_time']

    def __str__(self):
        return self.name


class EmailVerifyRecord(models.Model):
    email_choices = (
        ('register', u'注册'),
        ('forget', u'找回密码'),
    )
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=email_choices, max_length=10, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = '邮箱'
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.email



# 留言板
class MessageBoard(BaseModels):
    name = models.CharField(max_length=20, verbose_name='昵称')
    email = models.EmailField(verbose_name='邮件')
    url = models.CharField(max_length=256, verbose_name='网址')
    comment = models.TextField(verbose_name='内容')
    number = models.PositiveIntegerField(default=0, verbose_name='留言数')

    def add_number(self):
        self.number += 1
        self.save(update_fields=['number'])

    class Meta:
        verbose_name = '留言板'
        verbose_name_plural = verbose_name
        ordering = ['create_time']

    def __str__(self):
        return self.name




