# coding: utf-8
from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    type_id = serializers.IntegerField(max_value=20)
    title = serializers.CharField(max_length=40)
    author = serializers.CharField(max_length=20)
    count = serializers.IntegerField(min_value=0)
    date = serializers.DateField()
    images = serializers.ImageField()
    description = serializers.CharField()
    content = serializers.CharField()
    category = serializers.StringRelatedField(read_only=True,allow_null=True)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type_id = validated_data.get('type_id', instance.type_id)
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.count = validated_data.get('count', instance.count)
        instance.date = validated_data.get('date', instance.date)
        instance.images = validated_data.get('images', instance.images)
        instance.content = validated_data.get('content', instance.content)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.save()

        return instance

    class Meta:
        model = Article
        fields = ('title','author','category','date','description','content')


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    url = serializers.URLField()
    comment = serializers.CharField()
    number = serializers.IntegerField()
    blogs = serializers.StringRelatedField(read_only=True, allow_null=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.url = validated_data.get('url', instance.url)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.number = validated_data.get('number', instance.number)
        instance.save()

        return instance

    class Meta:
        model = Comment
        fields = ('name','email','url','comment','blogs','number')