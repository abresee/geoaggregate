#!/usr/bin/env python
from os import walk, path, getcwd
from zipfile import ZipFile
from collections import defaultdict
import re,string,shutil


class District:
    regex = re.compile(r'(?P<district>[^(]+)\((?P<shortname>\w{2})\)\s\((?P<district_code>\d{2})\)')

    def __init__(self,district,shortname,district_code):
        shortname_len, code_len = 2,2
        assert (len(shortname) == shortname_len) and (len(district_code) == code_len)
        self.name = string.capwords(district.strip().strip('*'))
        self.shortname = shortname
        self.code = district_code
        self.records={}
    
    def __lt__(self,other):
        return self.name < other.name

    def __str__(self):
        return ", ".join([self.name, self.shortname, self.code])
    def add_record(self,record):
        self.records[record.code]=record.name

    def decode(self,code):
        if code == self.code:
            return self.name
        elif code in self.records:
            return record.name


class Record:
    regex = re.compile(r'(?P<county_code>\d{3})\s+(?P<county>([^\d]+))')
    def __init__(self,district,county,county_code):
        assert len(county_code) == 3
        self.name=string.capwords(county.strip().strip('*'))
        self.code=county_code
        self.district=district

    def __lt__(self,other):
        return self.name < other.name
    
    def __str__(self):
        return ", ".join([self.name, self.code])


mapping = {}
cur_district=None
with open('county_FIPS.txt') as instream:
    for line in instream:

        m = District.regex.match(line)
        if m:
            cur_district = District(**m.groupdict())
            mapping[cur_district.code]=(cur_district.name)
            continue

        for m in Record.regex.finditer(line): 
            if not cur_district:
                raise Exception("found a record but have no district")
            record = Record(cur_district,**m.groupdict())
            cur_district.add_record(record)
            mapping[cur_district.code+record.code]=(cur_district.name, record.name)

name_scheme = re.compile(r'tl_rd13_(?P<fips_code>\d{2,5})_(?P<feat_kind>[^.]+).zip')
paths = defaultdict(list)
skipped=[]
unzip_dir = 'extracted'
working_dir = getcwd()

start_dir = path.join(working_dir,'data')

for dirpath, dirnames, filenames in walk(start_dir):
    for filename in filenames:
        m = name_scheme.match(filename)
        if m:
            fips_code=m.group('fips_code')
            feat_kind=m.group('feat_kind')
            if fips_code in mapping:
                group_name = mapping[fips_code] 
                name,ext=path.splitext(filename)
                basename = path.basename(dirpath)
                zipname = path.join(dirpath,filename)
                zipplace = path.join(working_dir,unzip_dir,basename,name)
                if path.exists(zipplace):
                    print("{0} {group} has already been unzipped".format(zipname,group=group_name))
                else:   
                    print("Unzipping {0} to {1}".format(zipname,zipplace))
                    z = ZipFile(zipname)
                    z.extractall(zipplace)
            else:
                skipped.append(filename)   
