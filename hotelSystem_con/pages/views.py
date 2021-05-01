from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def room_list(request):
    return render(request, 'room_list.html')

def room_detail(request):
    return render(request, 'room.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')