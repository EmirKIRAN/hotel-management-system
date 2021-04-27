from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def hotels(request):
    return render(request, 'hotels.html')

def room_list(request):
    return render(request, 'room_list.html')

def room_detail(request):
    return render(request, 'room.html')