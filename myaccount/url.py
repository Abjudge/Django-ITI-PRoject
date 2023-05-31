

from django.urls import path

from  .views import *
urlpatterns = [
    path("", Login, name="Login"),
    path("Reg/", reg, name="reg"),
    path("Logout/", Logout, name="logout"),
]