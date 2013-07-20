#!/usr/bin/env python
import re
pattern = r'(?P<code>\d{3})\s{2}(?P<name>.{0,15})'

with open('county_FIPS.txt') as instream:
    lines=instream.readlines()

matches=[]
for line in lines:
    matches.append(re.findall(pattern,line)) 
    
