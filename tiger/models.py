# e.g. file: tl_rd13_<state county FIPS>_addr.dbf
class Addr(models.Model):
    tiger_id = models.IntegerField()
    from_house = models.CharField(max_length=12)
    to_house = models.CharField(max_length=12)
    side_flag = models.CharField(max_length=1)
    zip_code = models.CharField(max_length=5)
    plus_four = models.CharField(max_length=4)
    from_type = models.CharField(max_length=1)
    to_type = models.CharField(max_length=1)
    ar_id = models.CharField(max_length=22)
    mtfcc = models.CharField(max_length=5)

addr_mapping = {
    'tiger_id' : 'TLID',
    'from_house' : 'FROMHN',
    'to_house' : 'TOHN',
    'side_flag': 'SIDE',
    'zip_code' : 'ZIP',
    'plus_four' : 'PLUS4',
    'from_type' : 'FROMTYP',
    'to_type' : 'TOTYP',
    'ar_id' : 'ARID', 
    'mtfcc' : 'MTFCC'
}

class AddrFn(models.Model):
    arid = models.CharField(max_length=22)
    linear_id = models.CharField(max_length=22)

# e.g. file: tl_rd13_<state county fips>_edges.shp
class Edges(models.Model):
    tiger_id = models.IntegerField()
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    face_left = models.IntegerField()
    face_right = models.IntegerField()
    mtfcc = models.CharField(max_length=5)
    full_name = models.CharField(max_length=100)
    smid = models.CharField(max_length=22)
    add_from_left = models.CharField(max_length=12)
    add_to_left = models.CharField(max_length=12)
    add_from_right = models.CharField(max_length=12)
    add_to_right = models.CharField(max_length=12)
    zip_left = models.CharField(max_length=5)
    zip_right = models.CharField(max_length=5)
    feat_cat = models.CharField(max_length=1)
    hydro_flag = models.CharField(max_length=1)
    rail_flag = models.CharField(max_length=1)
    road_flag = models.CharField(max_length=1)
    other_flag = models.CharField(max_length=1)
    passage_flag = models.CharField(max_length=1)
    divided_road_flag = models.CharField(max_length=1)
    ext_type = models.CharField(max_length=1)
    track_type = models.CharField(max_length=1)
    decked_road = models.CharField(max_length=1)
    art_path = models.CharField(max_length=1)
    persist_flag = models.CharField(max_length=1)
    gcse_flag = models.CharField(max_length=1)
    offset_left_flag = models.CharField(max_length=1)
    offset_right_flag = models.CharField(max_length=1)
    from_tiger_node = models.IntegerField()
    to_tiger_node = models.IntegerField()

    geom = models.MultiLineStringField(srid=4269)
    objects = models.GeoManager()

edges_mapping = {
    'state_fips' : 'STATEFP',
    'county_fips' : 'COUNTYFP',
    'tiger_id' : 'TLID',
    'face_left' : 'TFIDL',
    'face_right' : 'TFIDR',
    'mtfcc' : 'MTFCC',
    'full_name' : 'FULLNAME',
    'smid' : 'SMID', # spatial metadata identifier
    'add_from_left' : 'LFROMADD',
    'add_to_left' : 'LTOADD',
    'add_from_right' : 'RFROMADD',
    'add_to_right' : 'RTOADD',
    'zip_left' : 'ZIPL',
    'zip_right' : 'ZIPR',
    'feat_cat' : 'FEATCAT',
    'hydro_flag' : 'HYDROFLG',
    'rail_flag' : 'RAILFLG',
    'road_flag' : 'ROADFLG',
    'other_flag' : 'OLFFLG', 
    'passage_flag' : 'PASSFLG',
    'divided_road_flag' : 'DIVROAD',
    'ext_type' : 'EXTTYP',
    'track_type' : 'TTYP',
    'decked_road' : 'DECKEDROAD',
    'art_path' : 'ARTPATH',
    'persist_flag' : 'PERSIST',
    'gsce_flag' : 'GSCEFLG',
    'offset_left_flag' : 'OFFSETL',
    'offset_right_flag' : 'OFFSETR',
    'from_tiger_node' : 'TNIDF',
    'to_tiger_node' : 'TNIDT',
    'geom' : 'LINESTRING'
}

# e.g. file: tl_rd13_<state county fips>_faces.shp
class Faces(models.Model):
    tiger_id = models.IntegerField()
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    tract = models.CharField(max_length=6)
    block_group = models.CharField(max_length=1)
    block = models.CharField(max_length=4)
    county_sub_fips = models.CharField(max_length=5)
    subminor_cd = models.CharField(max_length=5)
    concity_fips = models.CharField(max_length=5)
    place_fips = models.CharField(max_length=5)
    aiannh_fips = models.CharField(max_length=5)
    aiannh_census = models.CharField(max_length=4)
    comp_type = models.CharField(max_length=1)
    sub_fips = models.CharField(max_length=5)
    sub_census = models.CharField(max_length=3)
    anrc_fips = models.CharField(max_length=5)
    elem_school = models.CharField(max_length=5)
    sec_school = models.CharField(max_length=5)
    unified_school = models.CharField(max_length=5)
    urban_area = models.CharField(max_length=5)
    cd111_fips = models.CharField(max_length=2)
    cd113_fips = models.CharField(max_length=2)
    state_leg_upper = models.CharField(max_length=3)
    state_leg_lower = models.CharField(max_length=3)
    voting_dist = models.CharField(max_length=6)
    zcta = models.CharField(max_length=5)
    uga = models.CharField(max_length=5)
    land_water = models.CharField(max_length=1)
    offset = models.CharField(max_length=1)
    area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)

    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

faces_mapping = {
    'tiger_id' : 'TFID',
    'state_fips' : 'STATEFP10',
    'county_fips' : 'COUNTYFP10',
    'tract' : 'TRACTCE10',
    'block_group' : 'BLKGRPCE10',
    'block' : 'BLOCKCE10',
    'county_sub_fips' : 'COUSUBFP10',
    'subminor_cd' : 'SUBMCDFP10',
    'concity_fips' : 'CONCTYFP10',
    'place_fips' : 'PLACEFP10',
    'aiannh_fips' : 'AIANNHFP10',
    'aiannh_census' : 'AIANNHCE10',
    'comp_type' : 'COMPTYP10',
    'sub_fips' : 'TRSUBFP10',
    'sub_census' : 'TRSUBCE10',
    'anrc_fips' : 'ANRCFP10',
    'elem_school' : 'ELSDLEA10',
    'sec_school' : 'SCSDLEA10',
    'unified_school' : 'UNSDLEA10',
    'urban_area' : 'UACE10',
    'cd111_fips' : 'CD111FP',
    'cd113_fips' : 'CD113FP',
    'state_leg_upper' : 'SLDUST',
    'state_leg_lower' : 'SLDLST',
    'voting_dist' : 'VTDST10',
    'zcta' : 'ZCTASCE10',
    'uga' : 'UGACE10',
    'land_water' : 'LWFLAG',
    'offset' : 'OFFSET',
    'area' : 'ATOTAL',
    'lat' : 'INTPTLAT',
    'lon' : 'INTPTLON',
    'geom' : 'POLYGON'
}

class FeatNames(models.Model): 
    tlid = models.IntegerField()
    full_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    pre_dir_abrv = models.CharField(max_length=15)
    pre_type_abrv = models.CharField(max_length=50)
    pre_qual_abrv = models.CharField(max_length=15)
    suf_dir_abrv = models.CharField(max_length=50)
    suf_qual_abrv = models.CharField(max_length=15)
    pre_dir = models.CharField(max_length=2)
    pre_type = models.CharField(max_length=3)
    pre_qual = models.CharField(max_length=2)
    suf_dir = models.CharField(max_length=2)
    suf_type = models.CharField(max_length=3)
    suf_qual = models.CharField(max_length=3)
    linear_id = models.CharField(max_length=22)
    mtfcc = models.CharField(max_length=5)
    pa_flag = models.Charfield(max_length=1)

feat_names_mapping = {
    'tlid' : 'TLID',
    'full_name' : 'FULLNAME',
    'name' : 'NAME',
    'pre_dir_abrv' : 'PREDIRABRV',
    'pre_type_abrv' : 'PRETYPABRV',
    'suf_dir_abrv' : 'SUFDIRABRV',
    'suf_qual_abrv' : 'SUFQUALABR',
    'pre_dir' : 'PREDIR',
    'pre_type' : 'PRETYP',
    'pre_qual' : 'PREQUAL',
    'suf_dir' : 'SUFDIR',
    'suf_type' : 'SUFTYP',
    'suf_qual' : 'SUFQUAL',
    'linear_id' : 'LINEARID',
    'mtfcc' : 'MTFCC',
    'pa_flag' : 'PAFLAG'
}
class FacesAH(models.Model):
    tfid = models.IntegerField()
    area_id = models.CharField(max_length=22)

class AreaWater(models.Model):
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    ansi = models.CharField(max_length=8)
    area_id = models.CharField(max_length=22)
    name = models.CharField(max_length=100)
    mtfcc = models.CharField(max_length=5)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)

    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

area_water_mapping = {
    'state_fips' : 'STATEFP',
    'county_fips' : 'COUNTYFP',
    'ansi' : 'ANSICODE',
    'area_id' : 'HYDROID',
    'name' : 'FULLNAME',
    'mtfcc' : 'MTFCC',
    'land_area' : 'AREALAND',
    'water_area' : 'AREAWATER',
    'lat' : 'INTPTLAT',
    'lon' : 'INTPTLON',
    'geom' : 'MULTIPOLYGON'
}

#e.g. file; tl_rd13_<state county fips>_linearwater.shp
class Linearwater(models.Model):
    ansi = models.CharField(max_length=8)
    linear_id = models.CharField(max_length=22)
    full_name = models.CharField(max_length=100)
    art_path = models.CharField(max_length=1)
    mtfcc = models.CharField(max_length=5)
    geom = models.MultiLineStringField(srid=4269)
    objects = models.GeoManager()

linearwater_mapping = {
    'ansi' : 'ANSICODE',
    'linear_id' : 'LINEARID',
    'full_name' : 'FULLNAME',
    'art_path' : 'ARTPATH',
    'mtfcc' : 'MTFCC',
    'geom' : 'LINESTRING'
}

# e.g. file: tl_rd13_<state county fips>_roads.shp
class Roads(models.Model):
    linear_id = models.CharField(max_length=22)
    full_name = models.CharField(max_length=100)
    route_type = models.CharField(max_length=1)
    mtfcc = models.CharField(max_length=5)

    geom = models.MultiLineStringField(srid=4269)
    objects = models.GeoManager()

roads_mapping = {
    'linear_id' : 'LINEARID',
    'full_name' : 'FULLNAME',
    'route_type' : 'RTTYP',
    'mtfcc' : 'MTFCC'
}

# e.g. file: tl_rd13_<state county fips>_vtd10.shp
class VotingDist(models.Model):
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    voting_dist = models.CharField(max_length=6)
    geoid = models.CharField(max_length=11)
    voting_dist_flag = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    namelsad = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)

    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

voting_dist_mapping = {
    'state_fips' : 'STATEFP10',
    'county_fips' : 'COUNTYFP10',
    'voting_dist' : 'VTDST10',
    'name' : 'NAME10',
    'namelsad' : 'NAMELSAD10',
    'lsad' : 'LSAD10',
    'mtfcc' : 'MTFCC10',
    'func_status' : 'FUNCSTAT10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10',
    'geom' : 'POLYGON'
}
# e.g. file: tl_rd13_02_anrc10.shp
# note: by its very nature, this only applies to AK (02)
class Anrc(models.Model):
    anrc_fips = models.CharField(max_length=5)
    anrc_ansi = models.CharField(max_length=8)
    geo_id = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=100)
    class_fips = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.PolygonField(srid=4269)
    objects = models.GeoManager()

anrc_mapping = {
    'anrc_fips' : 'ANRCFP10',
    'anrc_ansi' : 'ANRCNS10',
    'geo_id': 'GEOID10',
    'name' : 'NAME10',
    'lsad' : 'LSAD10',
    'class_fips' : 'CLASSFP10',
    'mtfcc' : 'MTFCC10',
    'func_state' : 'FUNCSTAT10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10',
    'geom' : 'POLYGON'
}

# e.g. file: tl_rd13_<state fips>_facesal.dbf
# TODO: turn this into a field on a model
class FacesAL(models.Model):
    tfid = models.IntegerField()
    area_id = models.CharField(max_length=22)

faces_al_mapping = {
    'tfid' : 'TFID',
    'area_id' : 'AREAID'
}

# e.g. file: tl_rd13_<state fips>_cd11{n}.shp
# n in ['1', '3']
class CensusDist(models.Model):
    state_fips = models.CharField(max_length=2)
    dist_fips = models.CharField(max_length=2)
    geoid = models.CharField(max_length=4)
    namelsad = models.CharField(max_length=41)
    lsad = models.CharField(max_length=2)
    session = models.CharField(max_length=3)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

census_dist_mapping = {
    'state_fips' : 'STATEFP10',
    'dist_fips' : 'CD11{N}FP', # N in ['1','3']
    'geoid' : 'GEOID10',
    'namelsad' : 'NAMELSAD10',
    'lsad' : 'LSAD10',
    'session' : 'CDSESSN',
    'mtfcc' : 'MTFCC10',
    'func_status' : 'FUNCSTAT10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON'
}

# e.g. file: tl_rd13_<state fips>_state10.shp
class State(models.Model):
    region = models.CharField(max_length=2)
    division = models.CharField(max_length=2)
    state_fips = models.CharField(max_length=2)
    state_ansi = models.CharField(max_length=8)
    geoid = models.CharField(max_length=2)
    usps_code = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager() 

state_mapping = {
    'region' : 'REGION10',
    'division' : 'DIVISION10',
    'state_fips' : 'STATEFP10',
    'state_ansi' : 'GEOID10',
    'geoid' : 'GEOID10',
    'usps_code' : 'STUSPS10'
    'name' : 'NAME10',
    'lsad' : 'LSAD10',
    'mtfcc' : 'MTFCC',
    'func_status' : 'FUNCSTAT10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10', 
    'lon' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON'
}

#Consolidated city
# state_fips in [09, 13, 18, 21, 30, 47] 
# file: tl_rd13_<state_fips>_concity.shp
class Concity(models.Model):
    state_fips = models.CharField(max_length=2)
    concity_fips = models.CharField(max_length=5)
    concity_ansi = models.CharField(max_length=8)
    geoid = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    class_fips = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

concity_mapping = {
    'state_fips' : 'STATEFP10',
    'concity_fips' : 'CONCTYFP10',
    'concity_ansi' : 'CONCTYNS10',
    'geoid' : 'GEOID10',
    'name' : 'NAME10',
    'lsad' : 'LSAD10',
    'class_fips' : 'CLASSFP10',
    'mtfcc' : 'MTFCC10',
    'func_status' : 'FUNCSTAT10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON'
}

# e.g. file: tl_rd13_<state fips>_place10.shp
class Place(models.Model):
    state_fips = models.CharField(max_length=2)
    place_fips = models.CharField(max_length=5)
    place_ansi = models.CharField(max_length=8)
    geoid = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    class_fips = models.CharField(max_length=2)
    cbsa = models.CharField(max_length=1)
    necta = models.CharField(max_length=1)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land = models.FloatField()
    water = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

place_mapping = {
    'state_fips' : 'STATEFP10',
    'place_fips' : 'PLACEFP10',
    'place_ansi' : 'PLACENS10',
    'geoid' : 'GEOID10',
    'name' : 'NAME10',
    'lsad' : 'LSAD10',
    'class_fips' : 'CLASSFP10',
    'cbsa' : 'PCICBSA10',
    'necta' : 'PCINECTA10',
    'mtfcc' ; 'MTFCC10',
    'func_status' : 'FUNCSTAT10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON'
}

# e.g. file: tl_rd13_<state fips>_tabblock10.shp
class Tabblock(models.Model):
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    tract_code = models.CharField(max_length=6)
    tabblock_code = models.CharField(max_length=4)
    geoid = models.CharField(max_length=15)
    name = models.CharField(max_length=10)
    mtfcc = models.CharField(max_length=5)
    ur_indicator = models.CharField(max_length=1)
    ua_code = models.CharField(max_length=5)
    ua_type = models.CharField(max_length=1)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

tabblock_mapping = {
    'state_fips' : 'STATEFP10',
    'county_fips' : 'COUNTYFP10',
    'tract_code' : 'TRACTCE10',
    'tabblock_code' : 'BLOCKCE10',
    'geoid' : 'GEOID10',
    'name' : 'NAME10',
    'mtfcc' : 'MTFCC10',
    'ur_indicator' : 'UR10',
    'ua_code' : 'UACE10',
    'ua_type' : 'UATYP10',
    'func_status' : 'FUNCSTATUS10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLAT10'
}

# e.g. file: tl_rd13_<state fips>_uga10.shp
class UrbanGrowthArea(models.Model):
    state_fips = models.CharField(max_length=2)
    local_code = models.CharField(max_length=5)
    local_type = models.CharField(max_length=1)
    geoid = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area= models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

urban_growth_area_mapping = {
    'state_fips' : 'STATEFP10',
    'local_code' : 'UGACE10',
    'local_type' : 'UGATYP10',
    'geoid' : 'GEOID10',
    'name' : 'NAME10',
    'lsad' : 'LSAD10',
    'mtfcc' : 'MTFCC10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10'
}

# e.g. file: tl_rd13_<state fips>_county10.shp
class County(models.Model):
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    county_ansi = models.CharField(max_length=8)
    geoid = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    lsad0 = models.CharField(max_length=2)
    class_fips = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    csa_fips = models.CharField(max_length=3)
    cbsa_fips = models.CharField(max_length=5)
    met_div = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

county_mapping = {
    'state_fips' : 'STATEFP10',
    'county_fips' : 'COUNTYFP10',
    'county_ansi' : 'COUNTYNS10',
    'geoid' : 'GEOID10',
    'name' : 'NAME10',
    'lsad' : 'LSAD10',
    'class_fips' : 'CLASSFP10',
    'mtfcc' : 'MTFCC10',
    'csa_fips' : 'CSAFP10',
    'cbsa_fips' : 'CBSAFP10',
    'met_div' : 'METDIVFP10',
    'func_status' : 'FUNCSTAT10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON' 
}

# e.g. file: tl_rd13_<state fips>_cousub10.shp
class CountySub(models.Model):
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    sub_fips = models.CharField(max_length=5)
    sub_ansi = models.CharField(max_length=8)
    geoid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    class_fips = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    cnecta_fips = models.CharField(max_length=3)
    necta_fips = models.CharField(max_length=5)
    necta_div = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

county_sub_mapping = {
    'state_fips' : 'STATEFP10',
    'county_fips' : 'COUNTYFP10',
    'sub_fips' : 'COUSUBFP10',
    'sub_ansi' : 'COUSUBNS10',
    'geoid' : 'GEOID10',
    'name' : 'NAME10',
    'lsad' : 'LSAD10',
    'class_fips' : 'CLASSFP10',
    'mtfcc' : 'MTFCC10',
    'cnecta_fips' : 'CNECTAFP10',
    'necta_fips' : 'NECTAFP10',
    'necta_div' : 'NCTADVFP10',
    'func_status' : 'FUNCSTAT10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON'
}
# e.g. file: tl_rd13_{state_fips}_submcd10.shp
# state_fips
class SubminorCD(models.Model):
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    sub_fips = models.CharField(max_length=5)
    submcd_fips = models.CharField(max_length=5)
    submcd_ansi = models.CharField(max_length=8)
    geoid = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    class_fips = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_lenght=12)
    geom = models.PolygonField(srid=4269)
    objects = models.GeoManager()

subminor_cd_mapping = {
    'state_fips' : 'STATEFP10',
    'county_fips' : 'COUNTYFP10',
    'sub_fips' : 'COUSUBFP10',
    'submcd_fips' : 'SUBMCDFP10',
    'submcd_ansi' : 'SUBMCDNS10',
    'geoid' : 'GEOID10',
    'name' : 'NAME10',
    'lsad' : 'LSAD10',
    'class_fips' : 'CLASSFP10',
    'mtfcc' : 'MTFCC10',
    'func_status' : 'FUNCSTAT10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10',
    'geom' : 'POLYGON'
}

# e.g. file: tl_rd13_<state fips>_pointlm.shp
class Landmark(models.Model):
    state_fips = models.CharField(max_length=2)
    ansi_code = models.CharField(max_length=8)
    point_id = models.CharField(max_length=22)
    full_name = models.CharField(max_length=100)
    mtfcc = models.CharField(max_length=5)
    geom = models.MultiPointField(srid=4269)
    objects = models.GeoManager()

landmark_mapping = {
    'state_fips' : 'STATEFP',
    'ansi_code' : 'ANSICODE',
    'point_id' : 'POINTID',
    'full_name' : 'FULLNAME',
    'mtfcc' : 'MTFCC',
    'geom' : 'MULTIPOINT'
}

# e.g. file: tl_rd13_<state fips>_arealm.shp
class AreaLandmark(models.Model):
    state_fips = models.CharField(max_length=2)
    ansi_code = models.CharField(max_length=8)
    area_id = models.CharField(max_length=22)
    full_name = models.CharField(max_length=120)
    mtfcc = models.CharField(max_length=5)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

area_landmark_mapping = {
    'state_fips' : 'STATEFP',
    'ansi_code' : 'ANSICODE',
    'area_id' : 'AREAID',
    'full_name' : 'FULLNAME',
    'mtfcc' : 'MTFCC',
    'land_area' : 'ALAND',
    'water_area' : 'AWATER',
    'lat' : 'INTPTLAT',
    'lon' : 'INTPTLON'
}

#primary and secondary roads
# e.g. file: tl_rd13_<state fips>_prisecroads.shp
class PriSecRoads(models.Model):
    linear_id = models.CharField(max_length=22)
    full_name = models.CharField(max_length=100)
    route_type = models.CharField(max_length=1)
    mtfcc = models.CharField(max_length=5)
    geom = models.MultiLineStringField(srid=4269)
    objects = models.GeoManager()

pri_sec_roads_mapping = {
    'linear_id' : 'LINEARID',
    'full_name' : 'FULLNAME',
    'route_type' : 'RTTYP',
    'mtfcc' : 'MTFCC',
    'geom' : 'MULTILINESTRING'
}

# e.g. file: tl_rd13_<state fips>_bg10.shp
class BlockGroup(models.Model):
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    tract_code = models.CharField(max_length=6)
    block_group = models.CharField(max_length=1)
    geoid = models.CharField(max_length=12)
    namelsad = models.CharField(max_length=13)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

block_group_mapping = {
    'state_fips' : 'STATEFP10',
    'county_fips' : 'COUNTYFP10',
    'tract_code' : 'TRACTCE10',
    'block_group' : 'BLKGRPCE10',
    'namelsad' : 'NAMELSAD10',
    'mtfcc' : 'MTFCC',
    'func_status' : 'FUNCSTAT10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON'
} 


# model for 3 shapefiles: 
# tl_rd13_<state fips>_{t}sd10.shp
# t in ['el','sc','un']
class SchoolDist(models.Model):
    state_fips = models.CharField(max_length=2)
    local_code= models.CharField(max_length=5)
    geoid = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    grade_min = models.CharField(max_length=2)
    grade_max = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    school_dist_type = models.CharField(max_length=1)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

school_dist_mapping = {
    'state_fips' : 'STATEFP10',
    'local_code' : '{T}SDLEA10', # T in ['EL', 'SC', 'UN']
    'geoid' : 'GEOID10',
    'name' : 'NAME10',
    'lsad' : 'LSAD10',
    'grade_min' : 'LOGRADE10',
    'grade_max' : 'HIGRADE10',
    'mtfcc' : 'MTFCC10',
    'school_dist_type' : 'SDTYP10',
    'func_status' : 'FUNCSTAT10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON'
}

# e.g. file: tl_rd13_<state fips>_sld{t}.shp
# t in ['u', 'l']
class StateLeg(models.Model):
    state_fips = models.CharField(max_length=2)
    state_leg = models.CharField(max_length=3)
    geoid = models.CharField(max_length=5)
    namelsad = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    year = models.CharField(max_length=4) #legislative session year
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

state_leg_mapping = {
    'state_fips' : 'STATEFP',
    'state_leg' : 'SLD{T}ST', # T in ['U', 'L']
    'geoid' : 'GEOID',
    'namelsad' : 'NAMELSAD',
    'lsad' : 'LSAD',
    'year' : 'LSY',
    'mtfcc' : 'MTFCC',
    'funcstat' : 'FUNCSTAT',
    'land_area' : 'ALAND',
    'water_area' : 'AWATER',
    'lat' : 'INTPTLAT',
    'lon' : 'INTPTLON',
    'geom' : 'MULTIPOLYGON'
}
#American Indian / Alaska Native / Native Hawaiian area
class Aiannh10(models.Model):
    # census code
    aiannhce10 = models.CharField(max_length=4)

    # ANSI code
    aiannhns10 = models.CharField(max_length=8)

    # yet another identifier. what is this one for? a mystery
    geoid10 = models.CharField(max_length=5)

    # area name
    name10 = models.CharField(max_length=100)

    # another area name, with description?
    namelsad10 = models.CharField(max_length=100)

    # description code
    lsad10 = models.CharField(max_length=2)

    # FIPS class code
    classfp10 = models.CharField(max_length=2)

    # "2010 Census American Indian/Alaska Native/Native Hawaiian area 
    # reservation/statistical area or off-reservation trust land Hawaiian 
    # home land indicator" your guess is as good as mine
    comptyp10 = models.CharField(max_length=1)

    # "2010 Census American Indian/Alaska Native/Native Hawaiian area 
    # federal/state recognition flag" yeah i dunno
    aiannhr10 = models.CharField(max_length=1)

    # MAF / TIGER feature class code
    mtfcc10 = models.CharField(max_length=5)

    # functional status
    funcstat10 = models.CharField(max_length=1)

    # land area
    aland10 = models.FloatField()

    # water area
    awater10 = models.FloatField()

    # lat of an internal point
    intptlat10 = models.CharField(max_length=11)

    # lon of an internal point
    intptlon10 = models.CharField(max_length=12)

    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

# American Indian Tribal subdivision 
class Aitsn10(models.Model):
    # AIANNH census code
    aiannhce10 = models.CharField(max_length=4)

    # tribal subdivision code
    trsubce10 = models.CharField(max_length=3)

    # tribal subdivision ANSI code
    trsubns10 = models.CharField(max_length=8)

    # yet another identifier
    geoid10 = models.CharField(max_length=7)

    # name
    name10 = models.CharField(max_length=100)

    # name with description
    namelsad10 = models.CharField(max_length=100)

    # description code
    lsad10 = models.CharField(max_length=2)

    # FIPS class code
    classfp10 = models.CharField(max_length=2)

    # MAF/TIGER class code
    mtfcc10 = models.CharField(max_length=5)

    # functional status (what is this)
    funcstat10 = models.CharField(max_length=1)

    # land area
    aland10 = models.FloatField()

    # water area
    awater10 = models.FloatField()

    # lat of internal point
    intptlat10 = models.CharField(max_length=11)

    # long of internal point
    intptlon10 = models.CharField(max_length=12)

    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

# 111th congressional districts
class Cd111(models.Model):
    # state fips code
    statefp10 = models.CharField(max_length=2)

    # 111th congressional district FIPS code
    cd111fp = models.CharField(max_length=2)

    # identifier - concat of state fips code and 111th FIPS code
    geoid10 = models.CharField(max_length=4)

    # name with description
    namelsad10 = models.CharField(max_length=41)

    # description code
    lsad10 = models.CharField(max_length=2)

    # session code
    cdsessn = models.CharField(max_length=3)

    # MAF / TIGER class code
    mtfcc10 = models.CharField(max_length=5)

    # functional statue (?)
    funcstat10 = models.CharField(max_length=1)

    # land area
    aland10 = models.FloatField()

    # water area 
    awater10 = models.FloatField()
     
    # lat of internal point
    intptlat10 = models.CharField(max_length=11)

    # long of internal point
    intptlon10 = models.CharField(max_length=12)

    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

# 113th congressional districts
class Cd113(models.Model):
    # state fips code
    statefp = models.CharField(max_length=2)

    # 113th congressional district fips codes
    cd113fp = models.CharField(max_length=2)

    # identifier
    geoid = models.CharField(max_length=4)

    # name with description
    namelsad = models.CharField(max_length=41)

    # description code
    lsad = models.CharField(max_length=2)

    # session code
    cdsessn = models.CharField(max_length=3)

    # MTF/TIGER code
    mtfcc = models.CharField(max_length=5)

    # Functional status
    funcstat = models.CharField(max_length=1)

    # land area
    aland = models.FloatField()

    # water area
    awater = models.FloatField()

    # lat of internal point
    intptlat = models.CharField(max_length=11)

    # lon of internal point
    intptlon = models.CharField(max_length=12)

    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

# Military Installations
class Mil(models.Model):
    # ANSI code for the installation
    ansicode = models.CharField(max_length=8)

    # area landmark identifier
    areaid = models.CharField(max_length=22)

    # name
    fullname = models.CharField(max_length=100)

    # MTF/TIGER code
    mtfcc = models.CharField(max_length=5)

    # land area
    aland = models.FloatField()

    # water area
    awater = models.FloatField()

    # lat of internal point
    intptlat = models.CharField(max_length=11)

    # lon of internal point
    intptlon = models.CharField(max_length=12)

    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

# State
class State10(models.Model):
    # region code
    region10 = models.CharField(max_length=2)

    # division code
    division10 = models.CharField(max_length=2)

    # fips code
    statefp10 = models.CharField(max_length=2)

    # ANSI code
    statens10 = models.CharField(max_length=8)

    # identifier
    geoid10 = models.CharField(max_length=2)

    # postal service abbreviation
    stusps10 = models.CharField(max_length=2)

    # name
    name10 = models.CharField(max_length=100)

    # description code
    lsad10 = models.CharField(max_length=2)

    # MTF/TIGER class code
    mtfcc10 = models.CharField(max_length=5)

    # functional status
    funcstat10 = models.CharField(max_length=1)

    # land area
    aland10 = models.FloatField()
     
    # water area
    awater10 = models.FloatField()

    # lat of internal point
    intptlat10 = models.CharField(max_length=11)

    # long of internal point
    intptlon10 = models.CharField(max_length=12)

    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

# Urban areas
class Uac10(models.Model):
    # Urban area code
    uace10 = models.CharField(max_length=5)

    # identifier
    geoid10 = models.CharField(max_length=5)

    # name
    name10 = models.CharField(max_length=100)

    # name with description
    namelsad10 = models.CharField(max_length=100)

    # description code
    lsad10 = models.CharField(max_length=2)

    # MTF/TIGER class code
    mtfcc10 = models.CharField(max_length=5)

    # Urban area type
    uatyp10 = models.CharField(max_length=1)

    # Functional status
    funcstat10 = models.CharField(max_length=1)

    # land area
    aland10 = models.FloatField()

    # water area
    awater10 = models.FloatField()

    # lat of internal point
    intptlat10 = models.CharField(max_length=11)

    # long of internal point
    intptlon10 = models.CharField(max_length=12)

    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

#5-digit zip code tabulation area
class Zcta510(models.Model):

    #2010 5 digit zip code tabulation area code
    zcta5ce10 = models.CharField(max_length=5)
    
    #2010 5 digit zip code tabulation identifier (how is this different from above?)
    geoid10 = models.CharField(max_length=5)

    #2010 census FIPS 55 class code
    classfp10 = models.CharField(max_length=2)

    #MAF/TIGER feature class code
    mtfcc10 = models.CharField(max_length=5)

    #2010 census functional status (what is this?)
    funcstat10 = models.CharField(max_length=1)

    #2010 census land area
    aland10 = models.FloatField()
    
    #2010 census water area
    awater10 = models.FloatField()

    #2010 census lat of internal point
    intptlat10 = models.CharField(max_length=11)

    #2010 census long of internal point
    intptlon10 = models.CharField(max_length=12)

    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()
