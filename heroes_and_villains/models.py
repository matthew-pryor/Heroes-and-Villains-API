from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.


class Supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=999)

    class Super_type(models.IntegerChoices):

        Hero = 1
        Villain = 2

    super_type_id = models.IntegerField(choices=Super_type.choices)