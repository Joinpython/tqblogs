

from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from blogs.serializers import ArticleSerializer
from blogs.models import Article

from message.models import FreshNews, BlogsRecord
from message.serializers import FreshNewsSerializer, BlogsRecordSerializer

from movies.models import Movies, WatchMovies
from movies.serializers import MoviesSerializer, WatchMoviesSerializer

from study.models import Study
from study.serializers import StudySerializers


# 分页
class DatePager(PageNumberPagination):

    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000
    template = None


# 首页
class IndexView(APIView):

    def get(self, request, *args, **kwargs):

        fresh_list = Article.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = ArticleSerializer(instance=pager_list, many=True)

        return JsonResponse({'code': 200, 'message': serializer.data, 'safe': False})

    def post(self, request, *args, **kwargs):

        fresh_list = Article.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = ArticleSerializer(instance=pager_list, many=True)

        return JsonResponse({'code': 200, 'message': serializer.data, 'safe': False})


# 文章查询
class ArticleLookView(APIView):

    def get(self, request, *args, **kwargs):

        fresh_list = Article.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = ArticleSerializer(instance=pager_list, many=True)

        return JsonResponse({'code': 200, 'message': serializer.data, 'safe': False})

    def post(self, request, *args, **kwargs):

        fresh_list = Article.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = ArticleSerializer(instance=pager_list, many=True)

        return JsonResponse({'code': 200, 'message': serializer.data, 'safe': False})


# 新闻页
class FreshView(APIView):

    def get(self, request, *args, **kwargs):

        fresh_list = FreshNews.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = FreshNewsSerializer(instance=pager_list, many=True)

        return JsonResponse({'code':200,'message':serializer.data,'safe':False})

    def post(self, request, *args, **kwargs):

        fresh_list = FreshNews.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = FreshNewsSerializer(instance=pager_list, many=True)

        return JsonResponse({'code': 200, 'message': serializer.data, 'safe': False})


# 博客收录
class BlogsRecordView(APIView):

    def get(self, request, *args, **kwargs):

        fresh_list = BlogsRecord.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = BlogsRecordSerializer(instance=pager_list, many=True)

        return JsonResponse({'code':200,'message':serializer.data,'safe':False})

    def post(self, request, *args, **kwargs):

        fresh_list = BlogsRecord.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = BlogsRecordSerializer(instance=pager_list, many=True)

        return JsonResponse({'code': 200, 'message': serializer.data, 'safe': False})


# 电影推荐
class MoviesView(APIView):

    def get(self, request, *args, **kwargs):

        fresh_list = Movies.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = MoviesSerializer(instance=pager_list, many=True)

        return JsonResponse({'code':200,'message':serializer.data,'safe':False})

    def post(self, request, *args, **kwargs):

        fresh_list = Movies.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = MoviesSerializer(instance=pager_list, many=True)

        return JsonResponse({'code': 200, 'message': serializer.data, 'safe': False})


# 观影小站
class WatchMoviesView(APIView):

    def get(self, request, *args, **kwargs):

        fresh_list = WatchMovies.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = WatchMoviesSerializer(instance=pager_list, many=True)

        return JsonResponse({'code':200,'message':serializer.data,'safe':False})

    def post(self, request, *args, **kwargs):

        fresh_list = WatchMovies.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = WatchMoviesSerializer(instance=pager_list, many=True)

        return JsonResponse({'code': 200, 'message': serializer.data, 'safe': False})


#　下载资源
class StudyView(APIView):

    def get(self, request, *args, **kwargs):

        fresh_list = Study.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = StudySerializers(instance=pager_list, many=True)

        return JsonResponse({'code':200,'message':serializer.data,'safe':False})

    def post(self, request, *args, **kwargs):

        fresh_list = Study.objects.all().order_by('-create_time')
        pager = DatePager()

        pager_list = pager.paginate_queryset(queryset=fresh_list, request=request, view=self)
        pager.get_previous_link()

        serializer = StudySerializers(instance=pager_list, many=True)

        return JsonResponse({'code': 200, 'message': serializer.data, 'safe': False})














