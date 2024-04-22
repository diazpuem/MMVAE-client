import pandas as pd
import plotly.express as px
from plotly.offline import plot

def bar_plot(df, label_x, label_y, title):
    fig = px.line(df, x=label_x, y=label_y, title= title)
    plot_div = plot(fig, output_type='div')
    return plot_div

def box_plot(label_x, label_y, title):
    df = px.data.iris()
    fig = px.box(df, x=label_x, y=label_y, title= title)
    plot_div = plot(fig, output_type='div')
    return plot_div