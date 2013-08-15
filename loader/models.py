from django.contrib.gis.db import models

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
        return ', '.join([self.name,self.parent.name])

class StateArchive(models.Model):
    state_equiv = models.ForeignKey('StateEquiv')

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

    feature = models.CharField(max_length=11, choices=FEATURE_CHOICES)

    def __str__(self):
        return ', '.join([self.feature, self.state_equiv.name])
