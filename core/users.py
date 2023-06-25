import json
from typing import Callable
from django.http import HttpResponse, JsonResponse
from core.serializers import UserRegistrationSerializer, UserCreateRequestSerializer
from core.models import User
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status


class UserRegistrationApiView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data.copy()
        data.pop("password")

        self.perform_create(serializer)

        return Response(data, status=status.HTTP_201_CREATED)

# def create_user(request):
#     if request.method != "POST":
#         raise ValueError("Only POST method is allowed")
#
#     user_create_serializer = UserRegistrationSerializer(data=json.loads(request.body))
#     is_valid = user_create_serializer.is_valid()
#
#     if not is_valid:
#         raise ValueError(user_create_serializer)
#
#     user = User.objects.create_user(**user_create_serializer.validated_data)
#     user_public_serializer = UserCreateRequestSerializer(user)
#
#     return JsonResponse(user_public_serializer.data)
