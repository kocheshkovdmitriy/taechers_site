from django.db import models

class New(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
