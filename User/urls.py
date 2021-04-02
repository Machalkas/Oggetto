from django.urls import path
from . import views

urlpatterns = [
    path('join', views.join, name="Join"),
    # path('login', views.logIn, name="Login"),
    path('logout', views.logOut, name="Login"),
]