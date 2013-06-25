import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, worldborder_mapping

our_path = os.path.abspath(os.path.join(os.path.dirname(__file__)

world_shp = os.path.join(our_path, 'data/TM_WORLD_BORDERS-0.3.shp')
census_blockgroups = os.path.join(out_path, 'data/CENSUS2010BLOCKGROUPS_POLY.shp') 

def run(verbose_=True):
    lm = LayerMapping(WorldBorder, world_shp, worldborder_mapping,
        transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose_)
