from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Hotel(models.Model):
    name = models.CharField(max_length=255,verbose_name='Otel ismi')
    slug = models.SlugField(max_length=50, unique=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.SET(get_sentinel_user), verbose_name='Otel sahibi')
    description = models.TextField(blank=True, null=True, verbose_name='Otel açıklaması')
    image = models.ImageField(upload_to="hotels/")
    address = models.CharField(max_length=255,verbose_name='Adres')
    country = models.CharField(max_length=50,verbose_name='Ülke')
    city = models.CharField(max_length=50, verbose_name='Şehir')

    def __str__(self):
        return self.name

class Room(models.Model):
    number = models.CharField(max_length=5,verbose_name="Oda numarası")
    number_of_beds = models.IntegerField(verbose_name="Yatak sayısı")
    price = models.FloatField(verbose_name="Oda fiyatı")
    image = models.ImageField(upload_to="rooms/")
    title = models.CharField(max_length=100, verbose_name="İçerik başlığı")
    detail = models.TextField(verbose_name="Oda detayları")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    



