#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module imports incidence rate date into the SQLite database.
@author: amberkiser
"""

def import_rate_data():
    """
    This method has no inputs and returns nothing.
    It imports data from the csv file to the SQLite tables VaxIncidenceRate
    and DiseaseChoices. These tables are defined as models in the vaxcharts
    app.
    """
    import pandas as pd
    import os
    import django

    os.environ['DJANGO_SETTINGS_MODULE'] = 'vaxtrends.settings'
    django.setup()
    from vaxcharts.models import VaxIncidenceRate, DiseaseChoices

    vpd_inc = pd.read_csv('import_data/reported_incidence.csv')
    pop = pd.read_csv('import_data/population.csv')

    vpd_rate = pd.merge(vpd_inc, pop, on='year')

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

    for row in vpd_rate.iterrows():
        vax = VaxIncidenceRate()
        vax.year = row[1]['year']
        vax.disease = row[1]['disease']
        vax.vaccine = row[1]['vaccine']
        vax.incidence_rate = row[1]['rate']
        vax.save()

    choices = vpd_rate['disease'].unique()
    choices.sort()

    for disease in choices:
        dis = DiseaseChoices()
        dis.disease = str(disease)
        dis.save()
        