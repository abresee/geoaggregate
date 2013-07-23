#!/usr/bin/env python
from collections import defaultdict
import re
import string

class District:
    regex = re.compile(r'(?P<district>[^(]+)\((?P<shortname>\w{2})\)\s\((?P<district_code>\d{2})\)')

    def __init__(self,district,shortname,district_code):
        shortname_len, code_len = 2,2
        assert (len(shortname) == shortname_len) and (len(district_code) == code_len)
        self.name = string.capwords(district.strip().strip('*'))
        self.shortname = shortname
        self.code = district_code
    
    def __lt__(self,other):
        return self.name < other.name

    def __str__(self):
        return "District: "+", ".join([self.name, self.shortname, self.code])

class Record:
    regex = re.compile(r'(?P<county_code>\d{3})\s+(?P<county>([^\d]+))')
    def __init__(self,county,county_code):
        assert len(county_code) == 3
        self.name=string.capwords(county.strip().strip('*'))
        self.code=county_code

    def __lt__(self,other):
        return self.name < other.name
    
    def __str__(self):
        return "County: "+", ".join([self.name, self.code])

matches = defaultdict(list)
district_save = None
record_save = None
comment = False

with open('county_FIPS.txt') as instream:
    for line in instream:
            continue
        district_match = District.regex.match(line)
        record_match = Record.regex.match(line)
        if district_match:
            current_district = District(**district_match.groupdict())
            district_save=district_match
            continue

        elif record_match:
            if not current_district:
                raise Exception("found a record but have no district")
            record = Record(**record_match.groupdict())
            record_save = record
            matches[current_district].append(record)
for district in sorted(matches):
    print(district)
    for county in sorted(matches[district]):
        print('\t',county)
