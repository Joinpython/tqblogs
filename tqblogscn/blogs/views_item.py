
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from blogs.models import Article, Comment
from blogs.serializers import ArticleSerializer, CommentSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
def index_item(request):
    if request.method == "POST":
        blogs = Article.objects.all()
        serializer = ArticleSerializer(blogs, many=True)

        return JsonResponse({'code':200, 'message':serializer.data, 'safe':False})

    # elif request.method == "POST":
    #     serializer = ArticleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def comment_item(request):
    if request.method == "GET":
        commoent = Comment.objects.all()
        serizlizer = CommentSerializer(commoent, many=True)

        return JsonResponse(serizlizer.data, safe=False)