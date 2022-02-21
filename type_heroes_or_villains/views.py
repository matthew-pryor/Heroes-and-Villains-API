from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import SuperTypeSerializer
from .models import SuperType

# Create your views here.

@api_view(['GET'])
def type_heroes_or_villains_list(request):

    if request.method == 'GET':

        super_types = SuperType.objects
        serializer = SuperTypeSerializer(super_types, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def type_heroes_or_villains_detail(request, pk):

    super_types = get_object_or_404(SuperType, pk=pk)