# Generated by Django 4.0 on 2022-10-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='grade',
            field=models.IntegerField(blank=True, default=0, verbose_name='Класс'),
        ),
    ]
