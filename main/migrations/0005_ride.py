# Generated by Django 2.2.6 on 2019-11-14 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20191105_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', mapbox_location_field.models.LocationField(map_attrs={})),
                ('destination', mapbox_location_field.models.LocationField(map_attrs={})),
                ('distance', models.FloatField(default=6.2, max_length=30)),
                ('cost', models.FloatField(default=250.0, max_length=30)),
                ('approved', models.BooleanField(default=False)),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
