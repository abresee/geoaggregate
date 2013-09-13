# states: county10, cousub 
# county: roads, linearwater
import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import SpatialReference
from tiger.models import County, CountySub, Roads, LineWater

extract_dir = 'travis_demo'
county_src = os.path.join(extract_dir,'tl_rd13_48_county10.shp')
srs = SpatialReference(4269)

load_tups = [
    (County, county_src)
]

for model, src in load_tups:
    lm = LayerMapping(model, src, model.mapping, source_srs=srs)
    lm.save(verbose=True)
