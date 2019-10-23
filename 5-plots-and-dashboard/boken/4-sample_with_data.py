import pandas as pd

player_stats = pd.read_csv('2017-18_playerBoxScore.csv', parse_dates=['gmDate'])
team_stats = pd.read_csv('2017-18_teamBoxScore.csv', parse_dates=['gmDate'])
standings = pd.read_csv('2017-18_standings.csv', parse_dates=['stDate'])

west_top_2 = (standings[(standings['teamAbbr'] == 'HOU') | (standings['teamAbbr'] == 'GS')]
        .loc[:, ['stDate', 'teamAbbr', 'gameWon']]
        .sort_values(['teamAbbr','stDate']))

print(west_top_2)

from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource

output_file('west-top-2-standings-race.html', 
            title='Western Conference Top 2 Teams Wins Race')

rockets_data = west_top_2[west_top_2['teamAbbr'] == 'HOU']
warriors_data = west_top_2[west_top_2['teamAbbr'] == 'GS']

rockets_cds = ColumnDataSource(rockets_data)
warriors_cds = ColumnDataSource(warriors_data)

fig = figure(x_axis_type='datetime',
             plot_height=300, plot_width=600,
             title='Western Conference Top 2 Teams Wins Race, 2017-18',
             x_axis_label='Date', y_axis_label='Wins',
             toolbar_location=None)

fig.step('stDate', 'gameWon', 
         color='#CE1141', legend='Rockets', 
         source=rockets_cds)
fig.step('stDate', 'gameWon', 
         color='#006BB6', legend='Warriors', 
         source=warriors_cds)

fig.legend.location = 'top_left'

show(fig)

# resources:
# https://docs.bokeh.org/en/latest/
# https://realpython.com/python-data-visualization-bokeh/
# https://www.kaggle.com/pablote/nba-enhanced-stats

