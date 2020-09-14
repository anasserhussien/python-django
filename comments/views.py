from django.shortcuts import render

from .models import Comment
from .serializers import *
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)

from rest_framework.mixins import (
    DestroyModelMixin,
    UpdateModelMixin
)

from .permissions import *
from rest_framework.permissions import (
    IsAuthenticated
)

# Create your views here.

class CommentDetailsAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentEditAPIView(RetrieveAPIView, DestroyModelMixin, UpdateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentEditSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    