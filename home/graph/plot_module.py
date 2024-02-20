import pandas as pd
import plotly.express as px
from plotly.offline import plot
import dash_bio

def bar_plot(df, label_x, label_y, title):
    fig = px.line(df, x=label_x, y=label_y, title= title)
    plot_div = plot(fig, output_type='div')
    return plot_div



def volcano_plot(df, label_x, label_y, title):
    fig = dash_bio.VolcanoPlot(
        dataframe = df,
        point_size = 10,
        effect_size_line_width = 4,
        genomewideline_width = 2,
        xlabel= label_x,
        ylabel= label_y,
        title= title,
    )
    plot_div = plot(fig, output_type='div')
    return plot_div
    