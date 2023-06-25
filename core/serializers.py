from rest_framework import serializers
from core.models import User, Message
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from core.roles import Role

user = get_user_model()


class UserCreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserCreateResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["email","password"]

    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        attrs["role"] = Role.USER
        return attrs


class LoginRequestSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=255, write_only=True)


class LoginResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    token = serializers.CharField()
