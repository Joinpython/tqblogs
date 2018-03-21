

from django.shortcuts import render


def fresh_news(request):

    return render(request, 'message/fresh_news.html')

def collect(request):

    return render(request, 'message/collect.html')