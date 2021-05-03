from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('dashboard/', views.user_dashboard, name="dashboard"),
    path('logout/', views.user_logout, name="logout"),
    path('reservations/', views.user_reservations, name="reservations"),
    path('create/', views.user_create_hotel, name="hotel_create"),
    path('update/<slug:hotel_slug>', views.user_update_hotel, name="update_hotel"),
    path('<slug:hotel_slug>/', views.hotel_detail, name="hotel_detail"),
    path('<slug:hotel_slug>/<int:room_id>/', views.delete_room, name="delete_room"),
]