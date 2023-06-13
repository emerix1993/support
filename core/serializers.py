from rest_framework import serializers
from core.models import User, Message


class UserCreateRequestSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=255, write_only=True)


class LoginResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    token = serializers.CharField()

