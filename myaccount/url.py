

from django.urls import path

from  .views import *
urlpatterns = [
    path("", Login, name="Login"),
    path("Reg/", reg, name="reg"),
    path("Logout/", Logout, name="logout"),
    path("List/", userlist, name="userlist"),
    path("RegAdmin/", RegAdmin, name="RegAdmin"),
    path("RegAdminModel/", RegAdminModel, name="RegAdminModel"),
]