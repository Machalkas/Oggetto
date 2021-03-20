from django.urls import path
from . import views

urlpatterns = [
    # path('', views.listSt, name="listStream"),
    path('', views.list.as_view()),
    path('create', views.create.as_view(), name="createStream"),
    # path('view/<st_id>', views.view, name="viewStream"),
]