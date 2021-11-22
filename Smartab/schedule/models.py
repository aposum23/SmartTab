from django.db import models
from django.contrib.auth.models import AbstractUser


class Table(models.Model):
    day = models.DateTimeField()
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=250)
    full_desc = models.CharField(max_length=1000)
    coord = models.CharField(max_length=500)
    status_made = models.BooleanField()


class UserSettings(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=200)
    image = models.ImageField()
    background = models.ImageField()


class Friends(models.Model):
    friend_id = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)


class PlansWithFriends(models.Model):
    friend_id = models.ForeignKey(Friends, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Shedule, on_delete=models.CASCADE)
# Create your models here.
