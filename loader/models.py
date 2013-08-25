from django.contrib.gis.db import models
from django.contrib.gis.utils import ogrinspect
from django.conf import settings
from zipfile import ZipFile, is_zipfile
from os import makedirs
from urllib import request
from math import ceil
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

class DownloadError(Exception):
    pass

class ExtractionError(Exception):
    pass

class ModelError(Exception):
    pass


class Archive(models.Model):
    class Meta:
        abstract = True

    name_template = 'tl_rd13_{code}_{feature}.zip'
    modelcache = {}

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
    def extract_path(self):
        return os.path.join(
            settings.MEDIA_ROOT,
            'extract',
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

    def set_size(self):
        with urllib.request.urlopen(self.url) as r:
            size = int(r.info().get('Content-length'))
        self.size = size
        self.save()

    def download(self):
        if not self.exists:
            self._download()
        return self.good

    def _download(self):
        os.makedirs(os.path.dirname(self.path),exist_ok=True)
        print('downloading {0}'.format(self.path))
        block = 4096
        print("{0} blocks".format(ceil(size/block)))
        written = 0
        with open(self.path,'wb') as dest:
            while True:
                data = r.read(block)
                if data:
                    dest.write(data)
                    written+=block
                    print("written: {0}\r".format(written),end='')
                else:
                    break

    def extract(self):
        if not self.exists:
            if not self.download():
                raise DownloadError("can't get {0}".format(str(self)))
        if self.extracted:
            print('already unzipped {0}'.format(str(self)))
            return True
        z = ZipFile(self.path)
        z.extractall(self.extract_path)
        return True

    @property
    def extracted(self):
        return os.path.exists(self.extract_path)

    @property
    def model(self):
        if self.feature not in Archive.modelcache:
            return self._get_model()
        else:
            return Archive.modelcache[self.feature]
    def _get_model(self):
        if not self.extracted:
            if not self.extract():
                raise ExtractionError("can't extract {0}".format(str(self)))

        #TODO: make this less shitty
        shps = [
            os.path.join(self.extract_path,filename) 
            for filename in os.listdir(self.extract_path) 
            if filename.endswith('shp')
        ]
        assert len(shps) == 1
        filename = shps[0]

        name = self.feature.capitalize()
        model = ogrinspect(filename,name,srid=4269)
        if name in Archive.modelcache:
            if Archive.modelcache[name] == model:
                print('match')
                self._model = model
            else:
                raise ModelError("this shouldn't happen!")
        Archive.modelcache[self.feature] = model
        return model


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

    size = models.BigIntegerField(null=True)
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
    size = models.BigIntegerField(null=True)
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

    size = models.BigIntegerField(null=True)

    class _extent:
        def __str__(self):
            return self.name
        name = 'National'
        code = 'us'

    extent = _extent()

    @property
    def folder(self):
        return 'nation'
