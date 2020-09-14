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


# Create your views here.

class CommentDetailsAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
