from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Place
from .serializers import PlaceSerializer


@api_view(['GET', 'POST'])
def places_list(request):
    if request.method == 'GET':
        places = Place.objects.all()
        serialized_places = PlaceSerializer(places, many=True)
        return Response(serialized_places.data)
    
    elif request.method == 'POST':
        serialized_place = PlaceSerializer(data=request.data)
        if serialized_place.is_valid():
            serialized_place.save()
            return Response(serialized_place.data, status=status.HTTP_201_CREATED)
        return Response(serialized_place.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def place_detail(request, pk):
    try:
        place = Place.objects.get(pk=pk)
    except Place.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialized_place = PlaceSerializer(place)
        return Response (serialized_place.data)
    
    elif request.method == 'PUT':
        serialized_place = PlaceSerializer(place, data=request.data)
        if serialized_place.is_valid():
            serialized_place.save()
            return Response(serialized_place.data)
        return Response(serialized_place.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serialized_place = PlaceSerializer(place, data=request.data, partial=True)
        if serialized_place.is_valid():
            serialized_place.save()
            return Response(serialized_place.data)
        return Response(serialized_place.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
