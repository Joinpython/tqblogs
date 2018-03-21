
# coding: utf-8
from rest_framework import serializers
from .models import Article, Comment


# 全部文章
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'create_time', 'type', 'count','title', 'author', 'category', 'date', 'description', 'content', 'images')


# 文章评论
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'create_time', 'name', 'email', 'url', 'comment', 'blogs', 'number')