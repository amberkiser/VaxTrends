#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module imports vaccine schedule history data from a csv file into the
SQLite database.
@author: amberkiser
"""

def import_history_data():
    """
    This method has no inputs and returns nothing.
    It imports data from the csv file to the SQLite table VaxHistory.
    This table is defined as a model in the vaxcharts app.
    """
    import pandas as pd
    import os
    import django

    os.environ['DJANGO_SETTINGS_MODULE'] = 'vaxtrends.settings'
    django.setup()
    from vaxcharts.models import VaxHistory

    cov = pd.read_csv('import_data/vaxhistory.csv')

    for row in cov.iterrows():
        vax = VaxHistory()
        vax.disease = row[1]['disease']
        vax.current_vaccine = row[1]['current_vaccine']
        vax.first_available = row[1]['first_available']
        vax.save()
