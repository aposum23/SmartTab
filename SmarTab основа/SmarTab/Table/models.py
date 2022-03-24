from django.db import models
from django.contrib.auth.models import User


#---------------Духно Михаил Александрович------------
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=150)
    desc = models.CharField(max_length=500)
    date = models.DateTimeField()
    coords = models.CharField(max_length=200)
    username = models.ForeignKey(User, on_delete=models.CASCADE)


class UserOptions(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    usr_img = models.ImageField(upload_to='static')
#----------misha.duhno@mail.ru---------------
