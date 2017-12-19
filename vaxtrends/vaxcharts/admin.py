from django.contrib import admin

from .models import VaxCoverage, VaxChoices, VaxIncidenceRate, DiseaseChoices

admin.site.register(VaxCoverage)
admin.site.register(VaxChoices)
admin.site.register(VaxIncidenceRate)
admin.site.register(DiseaseChoices)
