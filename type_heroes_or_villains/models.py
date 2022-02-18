from django.db import models

# Create your models here.

class Super_type(models.Model):

    class Super_type_id(models.IntegerChoices):

        Hero = 1
        Villain = 2

    alignment = models.IntegerField(choices=Super_type_id.choices)

    alignment_type = models.CharField(max_length=255)

    if alignment == 1:
        
        alignment_type = 'Hero'

    elif alignment == 2:

        alignment_type = 'Villain'