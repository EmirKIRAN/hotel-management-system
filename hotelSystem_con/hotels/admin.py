from django.contrib import admin
from . models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','owner', 'country')
    list_filter = ('country',)
    search_fields = ('name','owner')
