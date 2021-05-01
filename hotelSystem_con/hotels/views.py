from django.shortcuts import render
from . models import Hotel


def hotel_list(request):

    hotels = Hotel.objects.all().order_by('-id')

    context = {
        'hotels' : hotels
    }
    
    return render(request, 'hotels.html', context=context)
