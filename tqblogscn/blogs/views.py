import re
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from blogs.models import Article, Comment, MessageBoard, Category, Links

category = Category.objects.all()
link = Links.objects.all()
category = category[:6]
link = link[:4]


# @cache_page(60*15)
def index(request):
    blogs = Article.objects.all()
    article_list = blogs[:6]
    Carousel_map = Article.objects.get_article_by_create_time(limit=4, sort='new')

    context = {
        'article_list':article_list,
        'carousel':Carousel_map,
        'category': category,
        'link': link
    }
    return render(request, 'blogs/index.html', context)


@csrf_exempt
def detail(request,id):
    if request.method == 'POST':
        name = request.POST.get('author')
        email = request.POST.get('email')
        url = request.POST.get('url')
        comment = request.POST.get('comment')

        if not all([name, comment]):
            return JsonResponse({'code':200})

        if email:
            if not re.match(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$',str(email)):
                return JsonResponse({'code':201})

        if name:
            cont = Comment.objects.create_comment(author=name,
                                                  email=email,
                                                  comment=comment,
                                                  url=url,
                                                  blogs_id=id)
            cont.views_number()

            next_url = reverse('blogs:detail',args=(id,))
            return JsonResponse({'code':202,'next_url':next_url})


    if request.method == 'GET':
        blogs = Article.objects.get_article_by_id(article_id=id)
        blogs.views_count()

        blogs_list = Article.objects.all()
        article_list = blogs_list[:6]

        conent = Comment.objects.filter(blogs_id=id)
        return render(request, 'blogs/detail.html',{'blogs':blogs,
                                                    'content':conent,
                                                    'category': category,
                                                    'link': link,
                                                    'article_list':article_list,
                                                    })

def list(request, page):
    blogs = Article.objects.all()
    # 分页　每页显示10
    paginator = Paginator(blogs,10)
    num_page = paginator.num_pages

    if page == '' or int(page) > num_page:
        page = 1
    else:
        page = int(page)
    # 返回值是一个page类的实例对象
    blogs_list = paginator.page(page)

    if num_page < 5:
        pages = range(1,6)
    elif page <= 3:
        pages = range(num_page-4, num_page+1)
    else:
        pages = range(page-2, page+3)

    context = {
        'article_list':blogs_list,
        'blogs_list':blogs_list,
        'pages':pages,
        'category': category,
        'link': link
    }

    return render(request, 'blogs/list.html', context)


def article(request, page):
    blogs = Article.objects.all()
    # 分页　每页显示10
    paginator = Paginator(blogs, 10)
    num_page = paginator.num_pages

    if page == '' or int(page) > num_page:
        page = 1
    else:
        page = int(page)
    # 返回值是一个page类的实例对象
    blogs_list = paginator.page(page)

    if num_page < 5:
        pages = range(1, 6)
    elif page <= 3:
        pages = range(num_page - 4, num_page + 1)
    else:
        pages = range(page - 2, page + 3)

    context = {
        'article_list': blogs_list,
        'blogs_list': blogs_list,
        'pages': pages,
        'category': category,
        'link': link
    }

    return render(request, 'blogs/article.html',context)

@csrf_exempt
def messageboard(request):
    if request.method == "POST":
        name = request.POST.get('author')
        email = request.POST.get('email')
        url = request.POST.get('url')
        comment = request.POST.get('comment')

        if not all([name, comment]):
            return JsonResponse({'code': 200})

        if email:
            if not re.match(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$', str(email)):
                return JsonResponse({'code': 201})

        messageboard = MessageBoard.objects.create(name=name,
                                                   email=email,
                                                   url=url,
                                                   comment=comment,
                                                   number=0)

        next_url = reverse('blogs:messageboard')
        return JsonResponse({'code': 202, 'next_url': next_url})

    if request.method == 'GET':
        conent = MessageBoard.objects.all()
        conent = conent[:20]

        blogs = Article.objects.all()
        article_list = blogs[:6]

        return render(request, 'blogs/messageboard.html',{'content':conent,
                                                          'category': category,
                                                          'link': link,
                                                          'article_list':article_list
                                                          })



