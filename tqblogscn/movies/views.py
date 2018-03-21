


from django.shortcuts import render


def hot_movies(request):

    return render(request, 'movies/hot_movies.html')


def watch_movies_website(request):

    return render(request, 'movies/watch_movies_website.html')


