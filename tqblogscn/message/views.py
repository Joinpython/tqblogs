from django.shortcuts import render,HttpResponse

# Create your views here.


from message.models import BlogsRecord, FreshNews


def fresh_news(request):

    news_list = FreshNews.objects.order_by('-update_time')

    context = {
        'news_list':news_list
    }

    return render(request, 'message/fresh_news.html', context)

def collect(request):
    collect = BlogsRecord.objects.all()

    context = {
        'collect_blogs':collect
    }
    return render(request, 'message/collect.html', context)