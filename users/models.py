from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from users.managers import UserManager

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
