from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import sys
sys.path.append('..')
from hotels.models import Room,Hotel, Reservation

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'required' : 'required',
        'autofocus' : 'autofocus'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'required' : 'required',
        'data-eye' : 'data-eye'
    }))

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control bg-white border-left-0 border-md',
        'required' : 'required',
        'placeholder' : 'First name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control bg-white border-left-0 border-md',
        'required' : 'required',
        'placeholder' : 'Last name'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control bg-white border-left-0 border-md',
        'required' : 'required',
        'placeholder' : 'Username'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class' : 'form-control bg-white border-left-0 border-md',
        'required' : 'required',
        'placeholder' : 'Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control bg-white border-left-0 border-md',
        'required' : 'required',
        'placeholder' : 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control bg-white border-left-0 border-md',
        'required' : 'required',
        'placeholder' : 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']

class HotelCreateForm(forms.ModelForm):
    
    class Meta:
        model = Hotel
        fields = ['name','description','image','address','country','city']