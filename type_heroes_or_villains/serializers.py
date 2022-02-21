from rest_framework import serializers
from type_heroes_or_villains.models import SuperType
from .models import SuperType

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id','type']