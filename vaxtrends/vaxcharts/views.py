"""
This module defines the views that specify what will be displayed in the
html templates.
"""
from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, BoxZoomTool, ResetTool
import pandas as pd
from plotting import vaxplot, vpdplot
from vaxcharts.models import VaxCoverage, VaxIncidenceRate, VaxHistory
from .forms import CoverageForm, DiseaseForm

def index(request):
    """
    View that returns the home page.
    """
    return render(request, 'vaxcharts/home.html')

def coverage(request):
    """
    View that returns the vaccination coverage page.
    """
    form = CoverageForm(request.POST)
    vax = 'Dtap'
    if form.is_valid():
        vax = str(form.cleaned_data['vaccine'])

    all_data = pd.DataFrame.from_records(VaxCoverage.objects.all().values())

    plot_data = vaxplot.VaxPlot(df=all_data, color='black',
                                vaccine=vax, shade_color='#7570B3',
                                shade_alpha=0.2)

    if vax == 'No Vaccinations':
        ptitle = 'Children Age 19-35 Months Who Received No Vaccinations'
    else:
        ptitle = '%s Vaccination Coverage in Children Age 19-35 Months'%vax

    hover = HoverTool(tooltips=[
        ("Year", "$x{int}"),
        ("Coverage:", "$y"),
    ])

    plt = figure(plot_width=800, plot_height=400, tools=[hover], title=ptitle)

    plt.line(plot_data.x_values, plot_data.y_values, color=plot_data.color)
    plt.patch(plot_data.shadex_values, plot_data.shadey_values,
              color=plot_data.shade_color, fill_alpha=plot_data.shade_alpha,
              line_alpha=plot_data.shade_alpha)
    plt.xaxis.axis_label = "Year"
    plt.yaxis.axis_label = "Coverage"
    plt.add_tools(BoxZoomTool())
    plt.add_tools(ResetTool())

    script, div = components(plt)
    return render(request, 'vaxcharts/coverage.html',
                  {'script' : script, 'div' : div, 'form': form})

def schedule(request):
    """
    View that returns the immunization schedule page.
    """
    return render(request, 'vaxcharts/schedule.html')

def vpd(request):
    """
    View that returns the incidence rate page.
    """
    form = DiseaseForm(request.POST)
    disease = 'Chickenpox'
    if form.is_valid():
        disease = str(form.cleaned_data['disease'])

    all_data = pd.DataFrame.from_records(VaxIncidenceRate.objects.all().
                                         values())

    plot_data = vpdplot.VpdPlot(df=all_data, color='black', disease=disease)

    ptitle = 'Incidence Rate of %s per 100,000 Population'%disease
    hover = HoverTool(tooltips=[
        ("Year", "$x{int}"),
        ("Incidence Rate:", "$y"),
    ])

    plt = figure(plot_width=800, plot_height=400, tools=[hover], title=ptitle)

    plt.line(plot_data.x_values, plot_data.y_values, color=plot_data.color)
    plt.xaxis.axis_label = "Year"
    plt.yaxis.axis_label = "Incidence Rate per 100,000"
    plt.add_tools(BoxZoomTool())
    plt.add_tools(ResetTool())

    script, div = components(plt)

    data = VaxHistory.objects.all()

    return render(request, 'vaxcharts/vpd.html',
                  {'script' : script, 'div' : div, 'form': form, 'data':data})

def datasources(request):
    """
    View that returns the data sources page.
    """
    return render(request, 'vaxcharts/datasources.html')
