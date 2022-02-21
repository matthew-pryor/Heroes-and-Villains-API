from rest_framework import serializers
from type_heroes_or_villains.models import Super_type
from .models import Super_type

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super_type
        fields = ['type']