


from django.shortcuts import render
from movies.models import Movies, WatchMovies



def hot_movies(request):

    movie = Movies.objects.all().order_by('-create_time')

    context = {
        'movies':movie[:10]
    }

    return render(request, 'movies/hot_movies.html', context)


def watch_movies_website(request):

    return render(request, 'movies/watch_movies_website.html')


