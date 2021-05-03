# Generated by Django 3.2 on 2021-05-03 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0007_alter_hotel_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doing', to='hotels.room', verbose_name='Kiralanan Oda'),
        ),
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='do_joining', to='hotels.hotel'),
        ),
    ]