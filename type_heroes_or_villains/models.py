from django.db import models

# Create your models here.

class Super_type(models.Model):

    class Super_type_id(models.IntegerChoices):

        Hero = 1
        Villain = 2

    id = models.IntegerField(choices=Super_type_id.choices, primary_key=True)

    alignment = models.CharField(max_length=255)

    if id == 1:
        
        alignment = 'Hero'

    elif id == 2:

        alignment = 'Villain'