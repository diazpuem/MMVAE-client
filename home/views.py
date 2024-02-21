from django.shortcuts import render
from .graph.plot_module import bar_plot, volcano_plot
import pandas as pd

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
    
