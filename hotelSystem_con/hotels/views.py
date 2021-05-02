from django.shortcuts import render
from . models import Hotel, Room
from django.views.generic.list import ListView


class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels.html'
    context_object_name = 'hotels'
    queryset = Hotel.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Hotels'
        return context

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

def search(request):
    city = request.GET['city']
    hotel_name = request.GET['hotel']
    beds = request.GET['beds']

    hotels = Hotel.objects.filter(city__contains = city, name__contains = hotel_name)
    context = {
        'hotels' : hotels,
        'title' : 'Hotels'
    }
    return render(request, 'hotels.html', context=context)
