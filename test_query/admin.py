from django.contrib.gis import admin
from .models import WorldBorder, MACensusTract

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(MACensusTract, admin.OSMGeoAdmin)
