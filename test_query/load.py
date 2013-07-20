import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, worldborder_mapping, MACensusTract, macensustract_mapping

our_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

world_shp = os.path.join(our_path, 'data/TM_WORLD_BORDERS-0.3.shp')
census_tract_shp = os.path.join(our_path, 'data/CENSUS2010TRACTS_POLY.shp') 

def run(verbose_=True):
    #lm_border = LayerMapping(WorldBorder, world_shp, worldborder_mapping, transform=False, encoding='iso-8859-1')

    #lm_border.save(strict=True, verbose=verbose_)

    census_tracts = LayerMapping(MACensusTract, census_tract_shp, macensustract_mapping,
        transform=False, encoding='iso-8859-1')

    census_tracts.save(strict=True, verbose=verbose_)

