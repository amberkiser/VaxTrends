#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module imports vaccine coverage data from a csv file into 
the SQLite database.

@author: amberkiser
"""

# Full path and name to your csv file 
#csv_filepathname='vaxcov.csv'
#
#import os 
#import django
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'vaxtrends.settings' 
#django.setup()
#
#from vaxcharts.models import VaxCoverage 
#import csv 
#
#dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"') 
#
#for row in dataReader: 
#    if row[0] != 'year': 
#         #Ignore the header row, import everything else 
#        vax = VaxCoverage() 
#        vax.year = row[0] 
#        vax.vaccine= row[1] 
#        vax.ci_lower = row[2] 
#        vax.ci_upper = row[3] 
#        vax.coverage = row[4] 
#        vax.save() 

import pandas as pd
#import os 
#import django

#os.environ['DJANGO_SETTINGS_MODULE'] = 'vaxtrends.settings' 
#django.setup()
#from vaxcharts.models import VaxCoverage, VaxChoices

cov = pd.read_csv('vaxcov.csv')

#for row in cov.iterrows():
#    vax = VaxCoverage()
#    vax.year = row[1]['year']
#    vax.vaccine = row[1]['vaccine']
#    vax.ci_lower = row[1]['ci_lower']
#    vax.ci_upper = row[1]['ci_upper']
#    vax.coverage = row[1]['coverage']
#    vax.save()
    
choices = cov['vaccine'].unique()
choices.sort()
print(choices)

for vax in choices:
    print(type(str(vax)))

#for vax in choices:
#    vax = VaxChoices()
#    vax.vaccine = str(vax)
#    vax.save()
        