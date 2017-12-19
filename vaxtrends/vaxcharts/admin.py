"""
This module is where models are registers so that they can be accessed through
the admin site.
"""
from django.contrib import admin

from .models import VaxCoverage, VaxChoices, VaxIncidenceRate, DiseaseChoices,\
VaxHistory

admin.site.register(VaxCoverage)
admin.site.register(VaxChoices)
admin.site.register(VaxIncidenceRate)
admin.site.register(DiseaseChoices)
admin.site.register(VaxHistory)
