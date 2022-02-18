from dataclasses import field
from rest_framework import serializers

from type_heroes_or_villains.models import Super_type
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type', 'super_type_id']
        depth = 1

    super_type_id = serializers.IntegerField(write_only=True)