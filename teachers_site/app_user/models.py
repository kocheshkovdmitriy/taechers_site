from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=40, blank=True, verbose_name='Город проживания')
    school = models.CharField(max_length=200, blank=True, verbose_name='Школа')
    grade = models.IntegerField(blank=True, verbose_name='Класс')