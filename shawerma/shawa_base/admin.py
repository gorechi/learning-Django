from django.contrib import admin

from .models import District, Location, Place, PlaceRate

# Register your models here.
admin.site.register(District)
admin.site.register(Location)
admin.site.register(Place)
admin.site.register(PlaceRate)