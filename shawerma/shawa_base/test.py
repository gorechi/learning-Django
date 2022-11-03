from models import District, Location, Place, PlaceRate

from datetime import datetime
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from serializers import PlaceSerializer

place = Place.objects.first()
print(place)