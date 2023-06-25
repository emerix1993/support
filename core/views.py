import json
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.http import HttpResponse, JsonResponse
from core.serializers import UserRegistrationSerializer, LoginRequestSerializer


class UserRegistrationApiView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request)
