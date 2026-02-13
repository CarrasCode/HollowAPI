from django.urls import path

from ..views import LoginRequestView, UserRegistrationView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", LoginRequestView.as_view(), name="login"),
]
