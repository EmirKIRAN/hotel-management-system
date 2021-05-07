from django.shortcuts import render, get_object_or_404
from . models import Hotel, Room
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from . forms import ReservationForm
from django.urls import reverse_lazy


# ! hotels listed by their id's
# ! id numbers high to low
class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels.html'
    context_object_name = 'hotels'
    queryset = Hotel.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Hotels'
        return context

# rooms listed according to the received hotel slug parameter
# its filtered by hotel slug field
def index_hotel_detail(request, hotel_slug):
    rooms = Room.objects.filter(hotel__slug = hotel_slug)
    context = {
        'rooms':rooms,
        'title' : 'Rooms of hotel'
    }

    return render(request, 'room_list.html', context=context)

# The information about the room was brought according to the room number.
def room_detail(request, hotel_slug, room_id):
    room = Room.objects.get(hotel__slug=hotel_slug, id=room_id)
    context = {
        'room':room,
        'title' : 'Room detail'
    }

    return render(request, 'room.html', context=context)

# for search section under navbar area
# The search is performed by city name, number of beds and hotel name.

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

# this metod is for reservation process
class ReservationView(FormView):
    template_name = 'reservation.html'
    form_class = ReservationForm
    context_object_name = 'room'
    success_url = reverse_lazy('hotels')
    
    def form_valid(self, form):
        reservation = form.save(commit=False)
        _room = get_object_or_404(Room, id=self.kwargs['pk'])
        reservation.room = _room
        reservation.save()
        return super().form_valid(reservation)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = Room.objects.get(id = self.kwargs['pk'])
        context['title'] = 'Payment'
        return context
