from django.shortcuts import render

from movies.models import Movies, WatchMovies

def hot_movies(request):
    movies = Movies.objects.all()
    context = {
        'movies':movies
    }

    return render(request, 'movies/hot_movies.html', context)


def top_movies(request):
    movies = Movies.objects.all()
    context = {
        'movies':movies
    }

    return render(request, 'movies/top_movies.html', context)

def original_movies(request):
    movies = Movies.objects.all()
    context = {
        'movies':movies
    }

    return render(request, 'movies/original_movies.html', context)


def watch_movies_website(request):
    watch = WatchMovies.objects.all()
    context = {
        'watch_movies_website':watch
    }
    return render(request, 'movies/watch_movies_website.html', context)


