from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_list, name="hotels"),
    path('<slug:hotel_slug>/', views.hotel_detail, name="hotel_detail"),
    path('<slug:hotel_slug>/<int:room_id>/', views.room_detail, name="room_detail"),
]