# states: county10, cousub 
# county: roads, linearwater
from os import getenv, path
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import SpatialReference
from tiger.models import County, State

extract_dir = path.join(getenv('HOME'), 'travis_demo')
county_src = path.join(extract_dir,'tl_rd13_48_county10.shp')
state_src = path.join(extract_dir, 'tl_rd13_us_state10.shp')
srs = SpatialReference(4269)

load_tups = [
    (County, county_src),
    (State, state_src)
]

for model, src in load_tups:
    lm = LayerMapping(model, src, model.mapping, source_srs=srs)
    lm.save(verbose=True)
