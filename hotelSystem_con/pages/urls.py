from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hotels/', views.hotels, name="hotels"),
    path('roomlist/', views.room_list, name="room_list"),
    path('room/', views.room_detail, name="room"),
    path('login/', views.login, name="login"),
    path('register', views.register, name="register"),
]