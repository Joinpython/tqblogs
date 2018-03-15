
import xadmin
from study.models import Study

# Register your models here.

class StudyAdmin(object):
    list_display = ['title','create_time','url','password','abstract']
    list_per_page = 20

xadmin.site.register(Study, StudyAdmin)


