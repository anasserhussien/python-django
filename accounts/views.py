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

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

# Create your views here.

class UserCreateAPIView(CreateAPIView):
    query_set = User.objects.all()
    serializer_class = UserCreateSerializer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data = data)
        if serializer.is_valid(raise_exception = True ):
            new_data = serializer.data
            return Response(new_data, status = HTTP_200_OK)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
