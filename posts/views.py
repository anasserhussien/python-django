from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import Post
from .serializers import PostSerializer


# List all the posts
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Get detail of a specific post
class PostDetailsAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"

# Update a specific post
class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"

# Delete specific posts
class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"



