from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer
from rest_framework import status

# Create your views here.


@api_view(['POST'])
def createPost(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTHTTP)

@api_view(['GET'])
def getPosts(request):
    if request.method == 'POST':
        posts = Post.objects.all()
        serializer = PostSerializer(posts)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
