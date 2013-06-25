# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class WorldBorder(models.Model):
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.__unicode__()

# Auto-generated `LayerMapping` dictionary for WorldBorder model
worldborder_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'geom' : 'MULTIPOLYGON',
}

# This is an auto-generated Django model module created by ogrinspect.

class MACensus(models.Model):
    statefp10 = models.CharField(max_length=2)
    countyfp10 = models.CharField(max_length=3)
    tractce10 = models.CharField(max_length=6)
    blkgrpce10 = models.CharField(max_length=1)
    geoid10 = models.CharField(max_length=12)
    namelsad10 = models.CharField(max_length=13)
    mtfcc10 = models.CharField(max_length=5)
    aland10 = models.FloatField()
    awater10 = models.FloatField()
    intptlat10 = models.CharField(max_length=11)
    intptlon10 = models.CharField(max_length=12)
    area_sqft = models.FloatField()
    area_acres = models.FloatField()
    pop100_re = models.IntegerField()
    hu100_re = models.IntegerField()
    logpl94171 = models.CharField(max_length=7)
    logsf1 = models.IntegerField()
    logacs0610 = models.CharField(max_length=10)
    logsf1c = models.CharField(max_length=10)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for MACensus model
macensus_mapping = {
    'statefp10' : 'STATEFP10',
    'countyfp10' : 'COUNTYFP10',
    'tractce10' : 'TRACTCE10',
    'blkgrpce10' : 'BLKGRPCE10',
    'geoid10' : 'GEOID10',
    'namelsad10' : 'NAMELSAD10',
    'mtfcc10' : 'MTFCC10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'area_sqft' : 'AREA_SQFT',
    'area_acres' : 'AREA_ACRES',
    'pop100_re' : 'POP100_RE',
    'hu100_re' : 'HU100_RE',
    'logpl94171' : 'LOGPL94171',
    'logsf1' : 'LOGSF1',
    'logacs0610' : 'LOGACS0610',
    'logsf1c' : 'LOGSF1C',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTIPOLYGON',
}
