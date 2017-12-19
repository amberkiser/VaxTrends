#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: amberkiser
"""

import pandas as pd
#import os 
#import django

#os.environ['DJANGO_SETTINGS_MODULE'] = 'vaxtrends.settings' 
#django.setup()
#from vaxcharts.models import VaxIncidenceRate

vpd_inc = pd.read_csv('reported_incidence.csv')
pop = pd.read_csv('population.csv')

vpd_rate = pd.merge(vpd_inc, pop, on = 'year')

rate = []
for row in vpd_rate.iterrows():
    num = row[1]['reported_cases']
    if row[1]['disease'] == 'Hib (age < 5 yr)' or \
       row[1]['disease'] == 'Pneumococcal (age < 5 yr)':
        den = row[1]['population_under5']
    else:
        den = row[1]['population']
    rate.append(num / den * 100000)

vpd_rate['rate'] = rate

#print(vpd_rate.head())

choices = vpd_rate['disease'].unique()
choices.sort()

for c in choices:
    print(c)


#for row in vpd_rate.iterrows():
#    vax = VaxIncidenceRate()
#    vax.year = row[1]['year']
#    vax.disease = row[1]['disease']
#    vax.vaccine = row[1]['vaccine']
#    vax.incidence_rate = row[1]['rate']
#    vax.save()
