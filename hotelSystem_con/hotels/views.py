from django.shortcuts import render
from . models import Hotel, Room


def hotel_list(request):

    hotels = Hotel.objects.all().order_by('-id')

    context = {
        'hotels' : hotels,
        'title' : 'Hotels'
    }

    return render(request, 'hotels.html', context=context)

def hotel_detail(request, hotel_slug):
    rooms = Room.objects.filter(hotel__slug = hotel_slug)
    context = {
        'rooms':rooms,
        'title' : 'Rooms of hotel'
    }

    return render(request, 'room_list.html', context=context)

def room_detail(request, hotel_slug, room_id):
    room = Room.objects.get(hotel__slug=hotel_slug, id=room_id)
    context = {
        'room':room,
        'title' : 'Room detail'
    }

    return render(request, 'room.html', context=context)
