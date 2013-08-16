from django.contrib.gis.db import models
from django.conf import settings
from zipfile import ZipFile, is_zipfile
from os import makedirs
from urllib import request
import os.path

class Region(models.Model):
    '''Abstract base for the two fips region types'''
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

class StateEquiv(Region):
    '''A "state equivalent" district as fips 6-4 classifies them'''
    def __str__(self):
        return self.name

class CountyEquiv(Region):
    '''A "county equivalent" district as fips 6-4 classifies them'''
    parent = models.ForeignKey('StateEquiv')
    def __str__(self):
        return ', '.join([
            self.name,
            str(self.parent)
        ])

class Archive(models.Model):
    class Meta:
        abstract = True

    name_template = 'tl_rd13_{code}_{feature}.zip'

    @property
    def filename(self):
        return Archive.name_template.format(
            code = self.extent.code,
            feature = self.feature
        )

    @property
    def url(self):
        return 'ftp://ftp2.census.gov/geo/tiger/TIGERrd13_st/{folder}/{filename}'.format(
            folder = self.folder,
            filename = self.filename
        )

    @property
    def path(self):
        return os.path.join(
            settings.MEDIA_ROOT,
            self.folder,
            self.filename
        )

    @property
    def exists(self):
        return os.path.exists(self.path) and is_zipfile(self.path)

    @property
    def good(self):
        if not self.exists:
            return False
        z = ZipFile(self.path)
        return z.testzip() == None
        

    def download(self):
        if not self.exists:
            self._download()
        return self.good

    def _download(self):
        os.makedirs(os.path.dirname(self.path),exist_ok=True)
        with open(self.path,'wb') as dest:
            dest.write(request.urlopen(self.url).read())

    def __str__(self):
        return ', '.join([
            self.feature, 
            str(self.extent)
        ])

class CountyArchive(Archive):
    ADDR = 'addr'
    ADDRFN = 'addrfn'
    EDGES = 'edges'
    FACES = 'faces'
    FACESAH = 'facesah'
    FEATNAMES = 'featnames'
    LINEARWATER = 'linearwater'
    ROADS = 'roads'
    VTD10 = 'vtd10'

    FEATURE_CHOICES = (
        (ADDR, 'Address Ranges'),
        (ADDRFN, 'Address Range - Feature Name Relationships'),
        (EDGES, 'All Edges'),
        (FACES, 'Topological Faces'),
        (FACESAH, 'Topological Faces - Area Hydrography Relationships'),
        (FEATNAMES, 'Feature Names'),
        (LINEARWATER, 'Hydrography (Linear)'),
        (ROADS, 'Roads'),
        (VTD10, 'Voting Districts')
    )

    feature = models.CharField(
        max_length = len(max(FEATURE_CHOICES,key=lambda x: len(x[0]))[0]),
        choices = FEATURE_CHOICES,
    )

    extent = models.ForeignKey('CountyEquiv')

    @property
    def folder(self):
        return '/'.join([
            self.extent.parent.code,
            self.extent.code
        ])

class StateArchive(Archive):
    ANRC10 = 'anrc10'
    AREALM = 'arealm'
    BG10 = 'bg10'
    CD111 = 'cd111'
    CD113 = 'cd113'
    CONCITY10 = 'concity10'
    COUNTY10 = 'county10'
    COUSUB10 = 'cousub10'
    ELSD10 = 'elsd10'
    FACESAL = 'facesal'
    PLACE10 = 'place10'
    POINTLM  = 'pointlm'
    PRISECROADS = 'prisecroads'
    SCSD10 = 'scsd10'
    SLDL = 'sldl'
    SLDU = 'sldu'
    STATE10 = 'state10'
    SUBMCD10 = 'submcd10'
    TABBLOCK10 = 'tabblock10'
    TRACT10 = 'tract10'
    UGA10 = 'uga10'
    UNSD10 = 'unsd10'

    FEATURE_CHOICES = (
        (ANRC10, 'Alaska Native Regional Corporations'),
        (AREALM, 'Area Landmarks'),
        (BG10, 'Block Groups'),
        (CD111, '111th Congressional Districts'),
        (CD113, '113th Congressional Districts'),
        (CONCITY10, 'Consolidated Cities'),
        (COUNTY10, 'Counties'),
        (COUSUB10, 'County Subdivisions'),
        (ELSD10, 'Elementary School Districts'),
        (FACESAL, 'Relationships between Area Landmarks and Topological Faces'),
        (PLACE10, 'Places'),
        (POINTLM, 'Point Landmarks'),
        (PRISECROADS, 'Primary and Secondary Roads'),
        (SCSD10, 'Secondary School Districts'),
        (SLDL, 'State Legislative Lower Chamber Districts'),
        (SLDU, 'State Legislative Upper Chamber Districts'),
        (STATE10, 'States'),
        (SUBMCD10, 'Subminor Civil Divisions'),
        (TABBLOCK10, 'Blocks'),
        (UGA10, 'Urban Growth Areas'),
        (UNSD10, 'Unified School Districts')
    )

    feature = models.CharField(
        max_length = len(max(FEATURE_CHOICES,key=lambda x: len(x[0]))[0]),
        choices = FEATURE_CHOICES,
    )

    extent = models.ForeignKey('StateEquiv')

    @property
    def folder(self):
        return self.extent.code

class NationalArchive(Archive):
    AIANNH10 = 'aiannh10'
    AITSN10 = 'aitsn10'
    CD111 = 'cd111'
    CD113 = 'cd113'
    MIL = 'MIL' 
    STATE10 = 'state10'
    UAC10 = 'uac10'
    ZCTA510 = 'zcta510'

    FEATURE_CHOICES = (
        (AIANNH10, 'American Indian / Alaska Native / Native Hawaiian Areas'),
        (AITSN10, 'American Indian Tribal Subdivisions'),
        (CD111, '111th Congressional Districts'),
        (CD113, '113th Congressional Districts'),
        (MIL, 'Military Installations'),
        (STATE10, 'States'),
        (UAC10, 'Urban Areas'),
        (ZCTA510, 'Zip-code tabulation areas')
    )

    feature = models.CharField(
        max_length = len(max(FEATURE_CHOICES,key=lambda x: len(x[0]))[0]),
        choices = FEATURE_CHOICES
    )

    class _extent:
        def __str__(self):
            return self.name
        name = 'National'
        code = 'us'

    extent = _extent()

    @property
    def folder(self):
        return 'nation'
