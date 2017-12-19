#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module imports vaccine coverage data from a csv file into 
the SQLite database.

@author: amberkiser
"""

def import_coverage_data():
s        
    import pandas as pd
    import os 
    import django
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'vaxtrends.settings' 
    django.setup()
    from vaxcharts.models import VaxCoverage, VaxChoices
    
    cov = pd.read_csv('import_data/vaxcov.csv')
    
    for row in cov.iterrows():
        vax = VaxCoverage()
        vax.year = row[1]['year']
        vax.vaccine = row[1]['vaccine']
        vax.ci_lower = row[1]['ci_lower']
        vax.ci_upper = row[1]['ci_upper']
        vax.coverage = row[1]['coverage']
        vax.save()
        
    choices = cov['vaccine'].unique()
    choices.sort()
    
    for v in choices:
        vax = VaxChoices()
        vax.vaccine = str(v)
        vax.save()
        