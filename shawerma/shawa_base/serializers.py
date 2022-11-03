from rest_framework import serializers as se
from.models import Place, Shawa, District, Location, PlaceRate, Ingredient

class PlaceSerializer (se.Serializer):
    pk = se.IntegerField(read_only=True)
    name = se.CharField(max_length=200)
    description = se.CharField(style={'base_template': 'textarea.html'})
    url = se.URLField()
    creation_date = se.DateTimeField()
    address = se.CharField(max_length=300)
    #location
    #Нужно разобраться со связанными таблицами
    place_type = se.IntegerField()
    phone = se.CharField(max_length=20)
    delivery = se.BooleanField()
    seats = se.BooleanField()
    toilet = se.BooleanField()
    parking = se.BooleanField()
    order_by_phone = se.BooleanField()
    
    def create(self, validated_data):
        return Place.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.url = validated_data.get('url', instance.url)
        instance.address = validated_data.get('address', instance.address)
        #instance.location
        #Нужно разобраться со связанными таблицами
        instance.place_type = validated_data.get('place_type', instance.place_type)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.delivery = validated_data.get('delivery', instance.delivery)
        instance.seats = validated_data.get('seats', instance.seats)
        instance.toilet = validated_data.get('toilet', instance.toilet)
        instance.parking = validated_data.get('parking', instance.parking)
        instance.order_by_phone = validated_data.get('order_by_phone', instance.order_by_phone)
        instance.save()
        return instance
    
class PlaceRateSerializer(se.Serializer):
    pk = se.IntegerField(read_only=True)
    #place
    rate = se.IntegerField()
    creation_date = se.DateTimeField()
    change_date = se.DateTimeField()
    
    def create(self, validated_data):
        return Place.objects.create(**validated_data)
    
    def update (self, instance, validated_data):
        #place
        instance.rate = validated_data.get('rate', instance.rate)
        instance.change_date = validated_data.get('change_date', instance.change_date)
        instance.save()
        return instance

class IngredientSerializer(se.Serializer):
    pk = se.IntegerField(read_only=True)
    name = se.CharField(max_length=200)
    
    def create(self, validated_data):
        return Place.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class DistrictSerializer(se.Serializer):
    pk = se.IntegerField(read_only=True)
    name = se.CharField(max_length=200)
    description = se.CharField(style={'base_template': 'textarea.html'})
    creation_date = se.DateTimeField()
    
    def create(self, validated_data):
        return Place.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class LocationSerializer(se.Serializer):
    pk = se.IntegerField(read_only=True)
    name = se.CharField(max_length=200)
    description = se.CharField(style={'base_template': 'textarea.html'})
    creation_date = se.DateTimeField()
    #district
    
    def create(self, validated_data):
        return Place.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        #district
        instance.save()
        return instance

class ShawaSerializer(se.Serializer):
    pk = se.IntegerField(read_only=True)
    #place
    name = se.CharField(max_length=200)
    description = se.CharField(style={'base_template': 'textarea.html'})
    shawa_type = se.IntegerField()
    meat = se.IntegerField()
    size = se.IntegerField()
    creation_date = se.DateTimeField()
    spicy = se.BooleanField()
    #ingredients

    def create(self, validated_data):
        return Place.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        #place
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.shawa_type = validated_data.get('shawa_type', validated_data.shawa_type)
        instance.meat = validated_data.get('meat', validated_data.meat)
        instance.size = validated_data.get('size', validated_data.size)
        instance.spicy = validated_data.get('spicy', validated_data.spicy)
        #ingredients
        instance.save()
        return instance