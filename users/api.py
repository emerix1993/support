from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from users.serializers import UserCreateSerializer, UserPublicSerializer


class UserRegistrationApiView(CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        public_serializer = UserPublicSerializer(serializer.instance)
        return Response(public_serializer.data, status=status.HTTP_201_CREATED)
