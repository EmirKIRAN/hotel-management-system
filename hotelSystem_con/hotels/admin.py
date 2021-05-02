from django.contrib import admin
from . models import Hotel, Room, Reservation

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','owner', 'country')
    list_filter = ('country',)
    search_fields = ('name','owner')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('price','title')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('to_first_name','date')
