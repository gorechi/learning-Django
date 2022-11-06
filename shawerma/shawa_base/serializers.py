from rest_framework import serializers as se
from.models import Place, Shawa, District, Location, PlaceRate, Ingredient
        
class PlaceSerializer(se.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        depth = 2
        read_only_fields = ['pk', 'creation_date']
    
class PlaceRateSerializer(se.ModelSerializer):
    class Meta:
        model = PlaceRate
        fields = '__all__'
        depth = 1
        read_only_fields = ['pk', 'creation_date']

class IngredientSerializer(se.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
        depth = 1
        read_only_fields = ['pk']

class DistrictSerializer(se.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        depth = 1
        read_only_fields = ['pk', 'creation_date']

class LocationSerializer(se.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        depth = 1
        read_only_fields = ['pk', 'creation_date']

class ShawaSerializer(se.ModelSerializer):
    class Meta:
        model = Shawa
        fields = '__all__'
        depth = 1
        read_only_fields = ['pk', 'creation_date']