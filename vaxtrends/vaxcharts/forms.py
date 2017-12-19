from django import forms
from vaxcharts.models import VaxChoices, DiseaseChoices

class CoverageForm(forms.Form):
    vaccine = forms.ModelChoiceField(queryset=VaxChoices.objects.all(), 
                                     empty_label = None)
    
class DiseaseForm(forms.Form):
    disease = forms.ModelChoiceField(queryset=DiseaseChoices.objects.all(), 
                                     empty_label = None)
    