from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Отдельная страница со списком сообщений
    path('group/', views.group_posts),
    # Отдельная страница сообщения
    path('group/<slug:slug>/', views.post_detail),
]
