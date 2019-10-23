from bokeh.io import output_notebook, output_file
from bokeh.plotting import figure, show

output_file('sample.html', title='نمودار ساده')
fig = figure()

show(fig)