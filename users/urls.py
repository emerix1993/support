from django.urls import path
from users.api import UserRegistrationApiView

urlpatterns = [path("", UserRegistrationApiView.as_view())]

