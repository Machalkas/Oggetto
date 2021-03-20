from django.urls import path
from . import views

urlpatterns = [
    # path('create', views.create, name="createShop"),
    path('view', views.view.as_view()),
    path('create', views.create.as_view()),
]