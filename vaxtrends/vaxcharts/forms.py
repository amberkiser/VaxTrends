"""
This module holds the django forms defined for the vaxcharts app.
"""
from django import forms
from vaxcharts.models import VaxChoices, DiseaseChoices

class CoverageForm(forms.Form):
    """
    This form determines which vaccination coverage chart is shown.
    """
    vaccine = forms.ModelChoiceField(queryset=VaxChoices.objects.all(),
                                     empty_label=None)

class DiseaseForm(forms.Form):
    """
    This form determines which disease incidence rate chart is displayed.
    """
    disease = forms.ModelChoiceField(queryset=DiseaseChoices.objects.all(),
                                     empty_label=None)
