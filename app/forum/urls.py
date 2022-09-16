from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.createPost),
    path('get/', views.getPosts),
]