from django.shortcuts import render
from .graph.plot_module import bar_plot, volcano_plot
import pandas as pd
from django.http import HttpResponseRedirect
from .forms import GetAPIRequestData

def file(request):
    submitted = False
    if request.method == "POST" and ('_submit' in request.POST):
        form = GetAPIRequestData(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index?submitted=True')
    else:
        form = GetAPIRequestData
        if 'submitted' in request.GET:
            submitted = True
    return render(request, '/index.html', {'form':form, 'submitted':submitted})

def index(request):
    volcano_data = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/volcano_data1.csv')
    volcano_plot_div = volcano_plot(volcano_data, 'logFC', 'pvalue', 'Volcano Plot')
    context = {
        'volcano_plot_div': volcano_plot_div,
    }
    return render(request, 'index.html', context)

def graphs(request):
    volcano_data = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/volcano_data1.csv')
    bar_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
    bar_plot_div = bar_plot(bar_data, 'AAPL_x', 'AAPL_y', 'Apple Stocks')
    volcano_plot_div = volcano_plot(volcano_data, 'logFC', 'pvalue', 'Volcano Plot')

    context = {
            'bar_plot_div': bar_plot_div,
            'volcano_plot_div': volcano_plot_div,
        }
    return render(request, 'graphs.html', context)
    
