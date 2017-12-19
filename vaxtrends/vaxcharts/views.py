from django.shortcuts import render, render_to_response
#from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.models import HoverTool, BoxZoomTool, ResetTool 
from plotting import vaxplot, vpdplot
import pandas as pd
from vaxcharts.models import VaxCoverage, VaxIncidenceRate, VaxHistory
from .forms import CoverageForm, DiseaseForm

def index(request):
    return render(request, 'vaxcharts/home.html')

def coverage(request):
    form = CoverageForm(request.POST)
    vax = 'Dtap'
    if form.is_valid():
        vax = str(form.cleaned_data['vaccine'])
    
    all_data = pd.DataFrame.from_records(VaxCoverage.objects.all().values())



    plot_data = vaxplot.VaxPlot(df = all_data, color = 'black', 
                                         vaccine = vax, 
                                         shade_color = '#7570B3', 
                                         shade_alpha = 0.2)
    
    ptitle ='%s Vaccination Coverage in Children Age 19-35 Months'%vax
    hover = HoverTool(tooltips=[
        ("Year", "$x{int}"),    
        ("Coverage:", "$y"),
    ])
    
    p = figure(plot_width=800, plot_height=400, tools = [hover], 
               title = ptitle)
    
    p.line(plot_data.x_values, plot_data.y_values, color=plot_data.color)
    p.patch(plot_data.shadex_values, plot_data.shadey_values, 
            color=plot_data.shade_color, fill_alpha=plot_data.shade_alpha, 
            line_alpha=plot_data.shade_alpha)
    p.xaxis.axis_label = "Year"
    p.yaxis.axis_label = "Coverage"
    p.add_tools(BoxZoomTool())
    p.add_tools(ResetTool())

    script, div = components(p)
    return render(request, 'vaxcharts/coverage.html',
            {'script' : script , 'div' : div, 
             'form': form})
    
def schedule(request):
    return render(request, 'vaxcharts/schedule.html')

def vpd(request):
    form = DiseaseForm(request.POST)
    disease = 'Chickenpox'
    if form.is_valid():
        disease = str(form.cleaned_data['disease'])
    
    all_data = pd.DataFrame.from_records(VaxIncidenceRate.objects.all().values())

    plot_data = vpdplot.VpdPlot(df = all_data, color = 'black', 
                                disease = disease)
    
    ptitle ='Incidence Rate of %s per 100,000 Population'%disease
    hover = HoverTool(tooltips=[
        ("Year", "$x{int}"),    
        ("Incidence Rate:", "$y"),
    ])
    
    p = figure(plot_width=800, plot_height=400, tools = [hover], 
               title = ptitle)
    
    p.line(plot_data.x_values, plot_data.y_values, color=plot_data.color)
    p.xaxis.axis_label = "Year"
    p.yaxis.axis_label = "Incidence Rate per 100,000"
    p.add_tools(BoxZoomTool())
    p.add_tools(ResetTool())

    script, div = components(p)
    
    data = VaxHistory.objects.all()
    
    return render(request, 'vaxcharts/vpd.html',
            {'script' : script , 'div' : div, 
             'form': form, 'data':data})

def datasources(request):
    return render(request, 'vaxcharts/datasources.html')


