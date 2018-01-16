
import xadmin
from xadmin import views
from blogs.models import EmailVerifyRecord, Article, Tag, Category, Comment, MessageBoard, Links


class GlobalSetting(object):
    site_title = "博客管理系统"
    site_footer = "www.tqblogs.cn"
    menu_style = "accordion"

xadmin.site.register(views.CommAdminView, GlobalSetting)

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

class ArticleAdmin(object):
    list_display = ['title','date','author','category','tag','count']
    ordering = ['-count']
    list_per_page = 20
    style_fields = {"content": "ueditor"}

xadmin.site.register(Article, ArticleAdmin)

class CommentAdmin(object):
    list_display = ('name','blogs', 'create_time', 'number')
    ordering = ('-create_time',)
    list_per_page = 20

xadmin.site.register(Comment,CommentAdmin)

class TagAdmin(object):
    list_per_page = 20

xadmin.site.register(Tag, TagAdmin)


class CategoryAdmin(object):
    list_per_page = 20
xadmin.site.register(Category, CategoryAdmin)

class LinksAdmin(object):
    list_display = ['title','callback_url','description','date_publish']
    list_per_page = 10

xadmin.site.register(Links, LinksAdmin)


class MessageBoardAdmin(object):
    list_display = ('name', 'create_time', 'update_time', 'number')
    ordering = ('-create_time',)
    list_per_page = 20

xadmin.site.register(MessageBoard, MessageBoardAdmin)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
    menu_style = 'accordion'

xadmin.site.register(views.BaseAdminView, BaseSetting)
















