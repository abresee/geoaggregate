from django.contrib.gis.db import models
class Addr(models.Model):
    # e.g. file: tl_rd13_<state county FIPS>_addr.dbf
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
    # this field found in tl_rd13_<state county fips>_addrfn.dbf
    linear_id = models.CharField(max_length=22)

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
class Edges(models.Model):
    # e.g. file: tl_rd13_<state county fips>_edges.shp
    # TODO: clean up
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

# e.g. file: tl_rd13_<state fips>_facesal.dbf
# TODO: turn this into a field on a model
class FacesAL(models.Model):
    tfid = models.IntegerField()
    area_id = models.CharField(max_length=22)

faces_al_mapping = {
    'tfid' : 'TFID',
    'area_id' : 'AREAID'
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

#primary and secondary roads
# e.g. file: tl_rd13_<state fips>_prisecroads.shp
# TODO: figure if we even need this
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

class Faces(models.Model):
    # e.g. file: tl_rd13_<state county fips>_faces.shp
    # TODO: clean up
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
#TODO: figure out how necessary this is
    tiger_id = models.IntegerField()
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
    pa_flag = models.CharField(max_length=1)

feat_names_mapping = {
    'tiger_id' : 'TLID',
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
#TODO: make this a field
    tfid = models.IntegerField()
    area_id = models.CharField(max_length=22)

#### Places
class BasePlace(models.Model):
    class Meta:
        abstract = True
    land_area = models.FloatField()
    water_area = models.FloatField()
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()


class AreaWater(BasePlace):
    #TODO: eg
    state = models.ForeignKey('State')
    count = models.ForeignKey('County')
    ansi = models.CharField(max_length=8)
    area_id = models.CharField(max_length=22)
    name = models.CharField(max_length=100)
    mtfcc = models.CharField(max_length=5)

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
class CongressDist(BasePlace):
# e.g. file: tl_rd13_<state fips>_cd11{n}.shp
# n in ['1', '3']
    state_fips = models.CharField(max_length=2)
    dist_fips = models.CharField(max_length=2)

    geoid = models.CharField(max_length=4)
    lsad = models.CharField(max_length=2)
    session = models.CharField(max_length=3)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)

congresss_dist_mapping = {
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
class StateLegDist(BasePlace):
    # e.g. file: tl_rd13_<state fips>_sld{t}.shp
    # t in ['u', 'l']
    state_fips = models.CharField(max_length=2)
    state_leg = models.CharField(max_length=3)
    geoid = models.CharField(max_length=5)
    namelsad = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    year = models.CharField(max_length=4) #legislative session year
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)

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
class State(BasePlace):
    # e.g. file: tl_rd13_{state_fips}_state10.shp
    region = models.CharField(max_length=2)
    division = models.CharField(max_length=2)
    state_fips = models.CharField(max_length=2)
    state_ansi = models.CharField(max_length=8)
    usps_code = models.CharField(max_length=2)

    geoid = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)

    mapping = {
        'region' : 'REGION10',
        'division' : 'DIVISION10',
        'state_fips' : 'STATEFP10',
        'state_ansi' : 'GEOID10',
        'geoid' : 'GEOID10',
        'usps_code' : 'STUSPS10',
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
class Concity(BasePlace):
    # e.g. file: tl_rd13_{state_fips}_concity.shp
    #Consolidated city
    # state_fips in [09, 13, 18, 21, 30, 47] 
    # TODO: what is this
    state_fips = models.CharField(max_length=2)
    concity_fips = models.CharField(max_length=5)
    concity_ansi = models.CharField(max_length=8)
    geoid = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    class_fips = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)

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
class Place(BasePlace):
    # e.g. file: tl_rd13_{state_fips}_place10.shp
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
    'mtfcc' : 'MTFCC10',
    'func_status' : 'FUNCSTAT10',
    'land_area' : 'ALAND10',
    'water_area' : 'AWATER10',
    'lat' : 'INTPTLAT10',
    'lon' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON'
}
class Tabblock(BasePlace):
    #TODO: e.g.
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
class UrbanGrowthArea(BasePlace):
    # e.g. file: tl_rd13_{state_fips}_uga10.shp
    state_fips = models.CharField(max_length=2)
    local_code = models.CharField(max_length=5)
    local_type = models.CharField(max_length=1)
    geoid = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)

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

class County(BasePlace):
    # e.g. file: tl_rd13_{state_fips}_county10.shp
    class Meta(BasePlace.Meta):
        unique_together = ('state_fips','county_fips')
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    county_ansi = models.CharField(max_length=8)
    geoid = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    class_fips = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    csa_fips = models.CharField(max_length=3)
    cbsa_fips = models.CharField(max_length=5)
    met_div = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)

    def __str__(self):
        return ', '.join([self.name, self.state_fips])

    mapping = {
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
        'land_area' : 'ALAND10',
        'water_area' : 'AWATER10',
        'lat' : 'INTPTLAT10',
        'lon' : 'INTPTLON10',
        'geom' : 'MULTIPOLYGON' 
    }

class CountySub(BasePlace):
    # e.g. file: tl_rd13_{state_fips}_cousub10.shp
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

    mapping = {
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
class SubminorCD(BasePlace):
    # e.g. file: tl_rd13_{state_fips}_submcd10.shp
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
class VotingDist(BasePlace):
    # e.g. file: tl_rd13_<state county fips>_vtd10.shp
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    voting_dist = models.CharField(max_length=6)
    voting_dist_flag = models.CharField(max_length=1)

    geoid = models.CharField(max_length=11)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)

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
class AreaLandmark(BasePlace):
    # e.g. file: tl_rd13_<state fips>_arealm.shp
    state_fips = models.CharField(max_length=2)
    ansi_code = models.CharField(max_length=8)
    area_id = models.CharField(max_length=22)
    full_name = models.CharField(max_length=120)
    mtfcc = models.CharField(max_length=5)

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
class BlockGroup(BasePlace):
# e.g. file: tl_rd13_<state fips>_bg10.shp
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    tract_code = models.CharField(max_length=6)
    block_group = models.CharField(max_length=1)
    geoid = models.CharField(max_length=12)
    namelsad = models.CharField(max_length=13)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)

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
class SchoolDist(BasePlace):
    # model for 3 shapefiles: 
    # tl_rd13_<state fips>_{t}sd10.shp
    # t in ['el','sc','un']
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
class Anrc(BasePlace):
    # e.g. file: tl_rd13_02_anrc10.shp
    # note: by its very nature, this only applies to AK (02)
    class_fips = models.CharField(max_length=2)
    anrc_fips = models.CharField(max_length=5)
    anrc_ansi = models.CharField(max_length=8)

    geoid = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)

anrc_mapping = {
    'anrc_fips' : 'ANRCFP10',
    'anrc_ansi' : 'ANRCNS10',
    'geoid': 'GEOID10',
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
class AIANNHArea(BasePlace):
    # TODO: mapping
    #American Indian / Alaska Native / Native Hawaiian area
    aiannhce = models.CharField(max_length=4)
    aiannhns = models.CharField(max_length=8)
    geoid = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    class_fips = models.CharField(max_length=2)
    comptyp = models.CharField(max_length=1)
    aiannhr = models.CharField(max_length=1)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
class Aitsn10(BasePlace):
    # TODO: mapping
    # American Indian Tribal subdivision 
    aiannhce10 = models.CharField(max_length=4)
    trsubce10 = models.CharField(max_length=3)
    trsubns10 = models.CharField(max_length=8)
    geoid = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    class_fips = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    func_status = models.CharField(max_length=1)
class Mil(BasePlace):
    # TODO: mapping
    # Military Installations
    ansicode = models.CharField(max_length=8)
    areaid = models.CharField(max_length=22)
    fullname = models.CharField(max_length=100)
    mtfcc = models.CharField(max_length=5)
class UrbanArea(BasePlace):
    # TODO: mapping
    # Urban areas
    uace = models.CharField(max_length=5)
    geoid = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    uatyp10 = models.CharField(max_length=1)

    func_status = models.CharField(max_length=1)
class Zcta5(BasePlace):
    # TODO: mapping
    # 5-digit zip code tabulation area
    zcta5 = models.CharField(max_length=5)
    geoid = models.CharField(max_length=5)
    class_fips = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)

    func_status = models.CharField(max_length=1)

#### Lines
class BaseLine(models.Model):
    class Meta:
        abstract = True
    linear_id = models.CharField(max_length=22)
    full_name = models.CharField(max_length=100)
    mtfcc = models.CharField(max_length=5)
    geom = models.MultiLineStringField(srid=4269)
    objects = models.GeoManager()
class LineWater(BaseLine):
    #e.g. file; tl_rd13_<state county fips>_linearwater.shp
    art_path = models.CharField(max_length=1)
    ansi = models.CharField(max_length=8)

line_water_mapping = {
    'ansi' : 'ANSICODE',
    'linear_id' : 'LINEARID',
    'full_name' : 'FULLNAME',
    'art_path' : 'ARTPATH',
    'mtfcc' : 'MTFCC',
    'geom' : 'LINESTRING'
}
class Roads(BaseLine):
    # e.g. file: tl_rd13_<state county fips>_roads.shp
    route_type = models.CharField(max_length=1)

roads_mapping = {
    'linear_id' : 'LINEARID',
    'full_name' : 'FULLNAME',
    'route_type' : 'RTTYP',
    'mtfcc' : 'MTFCC'
}

