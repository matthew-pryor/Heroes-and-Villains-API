from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import SupersSerializer
from .models import Supers

# Create your views here.

@api_view(['GET', 'POST'])
def heroes_and_villains_list(request):
    
    if request.method == 'GET':

        supers = Supers.objects.all()
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)