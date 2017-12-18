from django.shortcuts import render, render_to_response
#from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.models import HoverTool
from plotting import allplot
import pandas as pd
from vaxcharts.models import VaxCoverage

def index(request):
    return render(request, 'vaxcharts/home.html')

def coverage(request):
    all_data = pd.DataFrame.from_records(VaxCoverage.objects.all().values())
    
    vax = 'Dtap'
    plot_data = allplot.VaxPlot(df = all_data, color = 'black', 
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

    script, div = components(p)
    return render_to_response( 'vaxcharts/coverage.html',
            {'script' : script , 'div' : div} )
#    return render(request, 'vaxcharts/coverage.html')
