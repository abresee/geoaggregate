#!/usr/bin/env python
''' 
lets download, unzip, gen models, and load!
'''
from zipfile import ZipFile
from django.contrib.gis.db import models
import yaml
import os
import re

with open('loader/fips.yaml') as fips_file:
    mapping = yaml.load(fips_file,yaml.CLoader)

class Extent(models.Model):
    name = models.CharField(max_length=255, unique=True)

class StateEquiv(Extent):
    id_str = models.CharField(max_length=2, unique=True)

class CountyEquiv(Extent):
    parent = models.ForeignKey('StateEquiv')
    id_str = models.CharField(max_length=3, unique=True)

class SpecialRegion(Extent):
    id_str = models.CharField(max_length=20, unique=True)

class DataSource(models.Model):
    extent = models.ForeignKey('Extent')
    path = models.CharField(max_length=255)
    
