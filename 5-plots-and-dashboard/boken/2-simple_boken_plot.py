from bokeh.io import output_notebook, output_file
from bokeh.plotting import figure, show

x = [1, 2, 3]
y = [1, 3, 2]

output_file('sample_plot.html', title='نمودار ساده')
fig = figure(title="نمودار ساده",
    plot_height=300, plot_width=300,
    x_range=(0, 3), y_range=(0, 3),
    toolbar_location=None)

fig.circle(x=x, y=y, color='green', size=9, alpha=0.6)

show(fig)