
import xadmin
from movies.models import Movies, WatchMovies

class MoviesAdmin(object):
    list_display = ('title', 'id','create_time','rate', 'url')
    list_per_page = 20

xadmin.site.register(Movies, MoviesAdmin)

class WatchMoviesAdmin(object):
    list_display = ('create_time', 'title', 'url', 'abstract')
    list_per_page = 20

xadmin.site.register(WatchMovies, WatchMoviesAdmin)





