from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import SuperTypeSerializer
from .models import Super_type

# Create your views here.

@api_view(['GET'])
def type_heroes_or_villains_list(request):

    if request.method == 'GET':

        super_types = Super_type.objects
        serializer = SuperTypeSerializer(super_types, many=True)
        return Response(serializer.data)