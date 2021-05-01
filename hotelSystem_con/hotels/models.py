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



