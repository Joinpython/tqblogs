

from rest_framework import serializers

from movies.models import Movies, WatchMovies


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = ('id','title','url','rate','images','abstract','create_time')


class WatchMoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchMovies
        fields = ('id','title','url','abstract','images','create_time',)



