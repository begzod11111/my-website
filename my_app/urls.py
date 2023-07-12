from .views import *
from django.urls import path


urlpatterns = [
    path("", home, name="home"),
    path("profile/", profile, name="profile"),
    path("reg/", AddUser.as_view(), name='reg')
]


