import re
from django.shortcuts import render,render_to_response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from blogs.models import Article, Comment, MessageBoard, Category, Links

from django.contrib.auth.models import User

category = Category.objects.all()
link = Links.objects.all()

#@cache_page(60*3)
def index(request):
    # blogs = Article.objects.get_article_by_create_time(limit=6, sort='new')
    # article_list = blogs[:6]
    Carousel_map = Article.objects.get_article_by_create_time(limit=6, sort='new')
    #
    context = {
        'carousel':Carousel_map,
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
    blogs = Article.objects.get_article_by_type(type_id=page,limit=10)
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


def categorys(request, page):
    blogs = Article.objects.get_article_by_category(category_id=page, limit=10)
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


@csrf_exempt
def page_not_found(request):
    return render_to_response('404.html')

@csrf_exempt
def page_error(request):
    return render_to_response('500.html')

def resume(request):
    return render(request, 'blogs/resume.html')


@csrf_exempt
def send_rest_email(request):
    email = request.POST.get('email')

    if email != '' and User.objects.filter(email=email):
        from django.core.mail import send_mail, EmailMultiAlternatives

        subject = 'hello'
        form_email = 'tqblogs@163.com'
        to_email = email
        text_content = 'This is an important message!!'
        html_content = u'<h1>激活链接：</h1><a href="http://www.tqblogs.cn" rel="external nofollow">漂泊在北京</a>'
        message = EmailMultiAlternatives(subject, text_content,form_email, [to_email])
        message.attach_alternative(html_content, 'text/html')
        message.send()

        # send_mail('修改密码', '您的新密码是：tqblogs','tqblogs@163.com',[email], fail_silently=False)

        print(email)

        return JsonResponse({'code':200})

    else:
        return JsonResponse({'code':201})
    # pass

