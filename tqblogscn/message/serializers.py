

from rest_framework import serializers
from message.models import FreshNews, BlogsRecord


class FreshNewsSerializer(serializers.ModelSerializer):

    class Meta:

        model = FreshNews
        fields = ('id', 'create_time', 'title', 'url', 'views', 'category')


class BlogsRecordSerializer(serializers.ModelSerializer):

    class Meta:

        model = BlogsRecord
        fields = ('id', 'create_time', 'title', 'url', 'images', 'abstract')








