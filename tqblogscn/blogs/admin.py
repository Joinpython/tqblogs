
import xadmin
from xadmin import views
from blogs.models import EmailVerifyRecord, Article, Category, Comment, MessageBoard, Links
from movies.models import Movies

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
    menu_style = 'accordion'

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSetting(object):
    site_title = "博客管理系统"
    site_footer = "黔ICP备17011880号-2"
    menu_style = "accordion"

xadmin.site.register(views.CommAdminView, GlobalSetting)

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

class ArticleAdmin(object):
    list_display = ['title','date','author','category','count']
    ordering = ['-count']
    list_per_page = 20
    style_fields = {"content": "ueditor"}

xadmin.site.register(Article, ArticleAdmin)

class CommentAdmin(object):
    list_display = ('name','blogs', 'create_time', 'number')
    ordering = ('-create_time',)
    list_per_page = 20

xadmin.site.register(Comment,CommentAdmin)

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























