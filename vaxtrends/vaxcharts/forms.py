from django import forms
from vaxcharts.models import VaxChoices

class CoverageForm(forms.Form):
    vaccine = forms.ModelChoiceField(queryset=VaxChoices.objects.all(), 
                                     empty_label = None)
    