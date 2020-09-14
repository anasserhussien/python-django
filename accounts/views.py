from django.shortcuts import render
from .models import *
from .serializers import *
#from django.contrib.auth import get_user_model as User


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

# from .permissions import *
from rest_framework.permissions import (
    IsAuthenticated
)

# Create your views here.

class UserCreateAPIView(CreateAPIView):
    query_set = User.objects.all()
    serializer_class = UserCreateSerializer
