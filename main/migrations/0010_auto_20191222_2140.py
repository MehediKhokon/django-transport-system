# Generated by Django 2.2.6 on 2019-12-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20191120_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='daily_rent',
            field=models.IntegerField(default=0),
        ),
    ]