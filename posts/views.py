from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)

from .models import Post
from .serializers import (
    PostSerializer, 
    PostCreateSerializer,
    PostListSerializer
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from .permissions import IsOwnerOrReadOnly


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



# List all the posts
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get_queryset(self, *args, **kwargs):
        query_list = Post.objects.all()
        query = self.request.GET.get("q")
        # sample query /posts/?q=test

        if query:
            query_list = query_list.filter(
                Q(title__icontains = query) |
                Q(content__icontains = query) |
                Q(user__username__icontains = query)
            ).distinct()
            return query_list  


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



