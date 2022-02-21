from type_heroes_or_villains.models import SuperType
from django.db import models

# Create your models here.


class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=999)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)