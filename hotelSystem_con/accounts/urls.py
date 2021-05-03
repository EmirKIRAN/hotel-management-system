from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('dashboard/', views.user_dashboard, name="dashboard"),
    path('create/', views.create_hotel, name="create_hotel"),
    path('logout/', views.user_logout, name="logout"),
    path('reservations/', views.user_reservations, name="reservations"),
    path('<slug:hotel_slug>/', views.hotel_detail, name="hotel_detail"),
]