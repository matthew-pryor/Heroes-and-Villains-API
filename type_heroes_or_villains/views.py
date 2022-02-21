from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import SuperTypeSerializer
from .models import SuperType

# Create your views here.

@api_view(['GET', 'POST'])
def type_heroes_or_villains_list(request):

    if request.method == 'GET':

        super_types = SuperType.objects
        serializer = SuperTypeSerializer(super_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def type_heroes_or_villains_detail(request, pk):

    super_types = get_object_or_404(SuperType, pk=pk)

    if request.method == 'GET':

        serializer = SuperTypeSerializer(super_types)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = SuperTypeSerializer(super_types, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == 'DELETE':

        super_types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)