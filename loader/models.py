#!/usr/bin/env python
''' 
lets download, unzip, gen models, and load!
'''
from zipfile import ZipFile
from collections import defaultdict
import os
import re
import yaml
import hashlib

class Record(yaml.YAMLObject):
    yaml_tag = '!Datafile'

    def __init__(self, extent, kind, path, prefix=None):
        self.extent = extent
        self.kind = kind
        self.origin = path
        self.prefix = prefix
    def __repr__(self):
        return "%s(extent=%r, kind=%r, origin=%r, prefix=%r)" % (
            self.__class__.__name__, 
            self.extent, self.kind, self.origin, self.prefix)

class Manifest(yaml.YAMLObject):
    yaml_tag = '!Manifest' 

    with open('fips.yaml') as fips_file:
        mapping = yaml.load(fips_file)

    def _rel_name(_,dirpath,filename):
        dirname = os.path.basename(dirpath)
        rel_name = os.path.join(dirname, filename)
        return rel_name

    def _scan(self, star_dir, prefix):
        if prefix:
            start_dir = os.path.join(start_dir,prefix)
        name_scheme = re.compile(
            r'tl_rd13_(?P<fips_code>\d{2,5})_(?P<feat_kind>[^.]+).zip')
        self.records = defaultdict(list)
        self.skipped = set()
        for dirpath, _, filenames in os.walk(start_dir):
            for filename in filenames:
                match = name_scheme.match(filename)
                if match:
                    m_dir = match.groupdict()
                    code = m_dir['fips_code']
                    if code in self.mapping:
                        extent = self.mapping[code]
                        kind = m_dir['feat_kind']
                        rel_name = self._rel_name(dirpath, filename)
                        record = Record(extent, kind, rel_name, prefix)
                        self.records[code].append(record)
                    else:
                        self.skipped.add(filename)
    @classmethod
    def from_file(cls, instream):
        return yaml.load(instream)

    def __repr__(self):
        return "%s(records=%r, skipped=%r)" % (
                self.__class__.__name__, self.records, self.skipped)
with open('manifest.yaml') as yamlfile:
    manifest = Manifest.from_file(yamlfile)


#def unzip(verbose=False):
#    '''
#    let's unzip
#    '''
#    unzip_dir = 'extracted'
#    working_dir = getcwd()
#
#    start_dir = path.join(working_dir,'data')
#    if True:
#        group_name = mapping[code] 
#        name, _ = path.splitext(filename)
#        zip_place = path.join(
#            working_dir, unzip_dir, dirname, name)
#        if path.exists(zip_place):
#            if verbose:
#                print(
#                    "{0} {group} has already been unzipped".format(
#                zip_name,group=group_name))
#        else:   
#            print("Unzipping ", zip_name)
#            zipfile = ZipFile(zip_name)
#            zipfile.extractall(zip_place)
#    else:
#        skipped.add(filename)   
#    return (skipped,manifest)
