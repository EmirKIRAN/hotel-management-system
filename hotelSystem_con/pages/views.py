from django.shortcuts import render


def index(request):
    return render(request, 'index.html',{'title':'main'})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')