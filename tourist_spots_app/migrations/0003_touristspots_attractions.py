# Generated by Django 2.2.3 on 2019-07-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions_app', '0001_initial'),
        ('tourist_spots_app', '0002_auto_20190715_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspots',
            name='attractions',
            field=models.ManyToManyField(to='attractions_app.Attraction'),
        ),
    ]
