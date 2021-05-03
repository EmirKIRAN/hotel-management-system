from django.shortcuts import render, redirect, get_object_or_404, Http404, HttpResponseRedirect
from . forms import LoginForm, RegisterForm, HotelCreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.text import slugify
import sys
sys.path.append('..')
from hotels.models import Room,Hotel, Reservation  


def user_login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
            else:
                messages.warning(request, 'Disabled accounts')
        else:
            messages.info(request, 'Check your username or password')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form':form})

def user_register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created !')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html',{'form':form})

@login_required(login_url='login')
def user_dashboard(request):
        
        current_user = request.user
        hotels = current_user.have_hotels.all()

        context = {
            'hotels': hotels,
            'title' : 'my dashboard',
        }
        return render(request, 'owner_index.html', context=context)

def user_logout(request):

    logout(request)
    return redirect('index')

@login_required(login_url='login')
def hotel_detail(request, hotel_slug):

    rooms = Room.objects.all().filter(hotel__slug=hotel_slug)
    current_hotel = Hotel.objects.get(slug=hotel_slug)

    context = {
        'rooms':rooms,
        'hotel':current_hotel
    }

    return render(request, 'hotel_detail.html',context=context)

@login_required(login_url='login')
def user_reservations(request):

    reservations = Reservation.objects.all().filter(room__hotel__owner__id = request.user.id)
    context = {
        'reservations':reservations,
        'title' : 'Reservations'
    }
    return render(request, 'reservations.html', context=context)

@login_required(login_url='login')
def delete_room(request, hotel_slug, room_id):
    _room = get_object_or_404(Room, id=room_id)
    _room.delete()
    return redirect('hotel_detail')

@login_required(login_url='login')
def user_create_hotel(request):

    form = HotelCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        hotel = form.save(commit=False)
        hotel.owner = request.user
        hotel.slug = slugify(hotel.name)
        hotel.save()
        return redirect('dashboard')

    context = {
        'form' : form,
        'title' : 'Create hotel',
        'btn' : 'Create'
    }
    return render(request, 'create_hotel.html', context=context)

@login_required(login_url='login')
def user_update_hotel(request, hotel_slug):

    current_hotel = get_object_or_404(Hotel, slug=hotel_slug)
    form = HotelCreateForm(request.POST or None, request.FILES or None, instance=current_hotel)
    if form.is_valid():
        hotel = form.save(commit=False)
        hotel.slug = slugify(hotel.name)
        hotel.save()
        return redirect('dashboard')

    context = {
        'form' : form,
        'title' : 'Update hotel',
        'btn' : 'Update'
    }
    return render(request, 'create_hotel.html', context=context)



