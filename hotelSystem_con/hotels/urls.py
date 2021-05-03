from django.urls import path
from . import views
from hotels.views import HotelListView, ReservationView

urlpatterns = [
    path('', HotelListView.as_view(), name="hotels"),
    path('search/', views.search, name="search"),
    path('reservation/<int:pk>/', ReservationView.as_view(), name="reservation"),
    path('<slug:hotel_slug>/', views.index_hotel_detail, name="index_hotel_detail"),
    path('<slug:hotel_slug>/<int:room_id>/', views.room_detail, name="room_detail"),
]