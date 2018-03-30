

from django.shortcuts import render


def fresh_news(request):

<<<<<<< HEAD
    return render(request, 'message/fresh_news.html')
=======
    news_list = FreshNews.objects.order_by('-create_time')

    context = {
        'news_list':news_list
    }

    return render(request, 'message/fresh_news.html', context)
>>>>>>> 1c828b9f5e97dabb1d9309c38940cd80c4c6003f

def collect(request):

<<<<<<< HEAD
    return render(request, 'message/collect.html')
=======
    context = {
        'collect_blogs':collect
    }
    return render(request, 'message/collect.html', context)
>>>>>>> 1c828b9f5e97dabb1d9309c38940cd80c4c6003f
