from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Place
from .serializers import PlaceSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data:dict={}, **kwargs) -> None:
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super().__init__(content, **kwargs)


@api_view(['GET', 'POST'])
def places_list(request):
    if request.method == 'GET':
        places = Place.objects.all()
        serialized_places = PlaceSerializer(places, many=True)
        return JSONResponse(serialized_places.data)
    
    elif request.method == 'POST':
        place_data = JSONParser().parse(request)
        serialized_place = PlaceSerializer(data=place_data)
        if serialized_place.is_valid():
            serialized_place.save()
            return JSONResponse(serialized_place.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serialized_place.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def place_detail(request, pk):
    try:
        place = Place.objects.get(pk=pk)
    except Place.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialized_place = PlaceSerializer(place)
        return JSONResponse (serialized_place.data)
    
    elif request.method == 'PUT':
        place_data = JSONParser().parse(request)
        serialized_place = PlaceSerializer(place, data=place_data)
        if serialized_place.is_valid():
            serialized_place.save()
            return JSONResponse(serialized_place.data)
        return JSONResponse(serialized_place.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        place_data = JSONParser().parse(request)
        serialized_place = PlaceSerializer(place, data=place_data, partial=True)
        if serialized_place.is_valid():
            serialized_place.save()
            return JSONResponse(serialized_place.data)
        return JSONResponse(serialized_place.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        place.delete()
        return JSONResponse(status=status.HTTP_204_NO_CONTENT)
