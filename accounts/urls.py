from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.sign_up, name="accounts.signup"),
    path("login/", views.login, name="accounts.login"),
    path("logout/", views.logout, name="accounts.logout"),
]