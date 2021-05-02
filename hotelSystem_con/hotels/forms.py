from django import forms
from . models import Reservation

class ReservationForm(forms.ModelForm):
    to_first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'required' : 'required'
    }))
    to_last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'required' : 'required'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'required' : 'required',
        'placeholder' : '1234 Main St'
    }))
    card_number = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'required' : 'required',
        'placeholder' : '**** **** *** *****'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'required' : 'required',
        'placeholder' : 'example@gmail.com'
    }))

    class Meta:
        model = Reservation
        fields = ['to_first_name', 'to_last_name', 'address', 'card_number', 'email']