from django.db import models
from core.head import UserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=255)
    role = models.PositiveSmallIntegerField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.email


class Request(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    visibility = models.BooleanField(default=True)
    status = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.RESTRICT,related_name="user_request")
    manager = models.ForeignKey(User, on_delete=models.RESTRICT,related_name="manager_request")

    class Meta:
        db_table = "requests"


class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.RESTRICT,related_name="messages")
    request = models.ForeignKey(Request, on_delete=models.RESTRICT,related_name="messages")

    class Meta:
        db_table = "messages"
