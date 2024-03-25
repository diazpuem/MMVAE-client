from django.shortcuts import render
from .graph.plot_module import bar_plot, volcano_plot
import pandas as pd
from django.http import HttpResponseRedirect
from .forms import GetAPIRequestData

#File upload 
def index(request):
    submitted = False
    if request.method == "POST":
        print("POST")
        form = GetAPIRequestData(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv']
            npz_file = form.cleaned_data['npz']
            form.save()
            return HttpResponseRedirect('/index?submitted=True')
        else:
            print(form.errors)
    else:
        form = GetAPIRequestData()
        if 'submitted' in request.GET:
            submitted = True
            
    context = {
        'submitted': submitted,
        'form': form,
    }
    return render(request, 'index.html', context)

#Filter graph view
def graphs(request):
    volcano_data = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/volcano_data1.csv')
    bar_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
    bar_plot_div = bar_plot(bar_data, 'AAPL_x', 'AAPL_y', 'Apple Stocks')
    volcano_plot_div = volcano_plot(volcano_data, 'logFC', 'pvalue', 'Volcano Plot')
    submitted = False
    
    context = {
            'bar_plot_div': bar_plot_div,
            'volcano_plot_div': volcano_plot_div,
        }
    return render(request, 'graphs.html', context)
    
