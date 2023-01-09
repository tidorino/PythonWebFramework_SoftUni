from django.contrib.auth import get_user_model
from rest_framework import generics as rest_views
from django.shortcuts import render

from ToDoApp.api_auth.serializers import CreateUserSerializer

UserModel = get_user_model()


class CreateUserApiView(rest_views.CreateAPIView):
    queryset = UserModel
    serializer_class = CreateUserSerializer


class LoginApiView:
    pass


class LogoutApiView:
    pass
