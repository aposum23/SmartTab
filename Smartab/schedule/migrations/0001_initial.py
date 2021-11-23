# Generated by Django 3.2.9 on 2021-11-22 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('title', models.CharField(max_length=150)),
                ('desc', models.CharField(max_length=250)),
                ('full_desc', models.CharField(max_length=1000)),
                ('coord', models.CharField(max_length=500)),
                ('status_made', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=150)),
                ('second_name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('background', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
