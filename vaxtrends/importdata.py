#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:41:01 2017

@author: amberkiser
"""

# Full path and name to your csv file 
#csv_filepathname="/home/mitch/projects/wantbox.com/wantbox/zips/data/zipcodes.csv" 
csv_filepathname='vaxcov.csv'
# Full path to your django project directory 
#your_djangoproject_home="/home/mitch/projects/wantbox.com/wantbox/" 
#your_djangoproject_home="/amberkiser/Code/VaxTrends/vaxtrends/vaxtrends/" 

import sys,os 
#sys.path.append(your_djangoproject_home) 
#print(sys.path.append(your_djangoproject_home) )
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'vaxtrends.settings' 
django.setup()
from vaxcharts.models import VaxCoverage 
import csv 
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"') 
for row in dataReader: 
#    print(row)
    if row[0] != 'year': 
         #Ignore the header row, import everything else 
        vax = VaxCoverage() 
        vax.year = row[0] 
        vax.vaccine= row[1] 
        vax.ci_lower = row[2] 
        vax.ci_upper = row[3] 
        vax.coverage = row[4] 
        vax.save() 
        