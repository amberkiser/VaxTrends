from django.contrib import admin

from .models import VaxCoverage, VaxChoices

admin.site.register(VaxCoverage)
admin.site.register(VaxChoices)
