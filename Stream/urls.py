from django.urls import path
from . import views

urlpatterns = [
    path('', views.listSt, name="listStream"),
    path('create', views.create, name="createStream"),
]