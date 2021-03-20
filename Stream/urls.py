from django.urls import path
from . import views

urlpatterns = [
    path('', views.listSt, name="listStream"),
    path('create', views.create, name="createStream"),
    path('view/<st_id>', views.view, name="viewStream"),
]