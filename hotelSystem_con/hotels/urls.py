from django.urls import path
from . import views
from hotels.views import HotelListView

urlpatterns = [
    path('', HotelListView.as_view(), name="hotels"),
    path('search/', views.search, name="search"),
    path('<slug:hotel_slug>/', views.hotel_detail, name="hotel_detail"),
    path('<slug:hotel_slug>/<int:room_id>/', views.room_detail, name="room_detail"),
]