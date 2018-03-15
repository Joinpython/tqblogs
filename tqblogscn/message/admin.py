
import xadmin
from message.models import BlogsRecord, FreshNews


class BlogsRecordAdmin(object):

    list_display = ['title','create_time', 'url', 'abstract']
    list_per_page = 20

xadmin.site.register(BlogsRecord, BlogsRecordAdmin)


class FreshNewsAdmin(object):
    list_display = ['title', 'create_time', 'views', 'url','category']
    list_per_page = 20

xadmin.site.register(FreshNews, FreshNewsAdmin)
