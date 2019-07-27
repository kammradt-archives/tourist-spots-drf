# Generated by Django 2.2.3 on 2019-07-27 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TouristSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='tourist_spots_images')),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses_app.Address')),
            ],
        ),
    ]
