#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module imports vaccine coverage data from a csv file into
the SQLite database.

@author: amberkiser
"""

def import_coverage_data():
    """
    This method has no inputs and returns nothing.
    It imports data from the csv file to the SQLite tables VaxCoverage and
    VaxChoices. These tables are defined as models in the vaxcharts app.
    """

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

    for vx in choices:
        vax = VaxChoices()
        vax.vaccine = str(vx)
        vax.save()
