import json
import unirest
import numpy as np
import pandas as pd
from math import pi
import bokeh
from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool,ColorMapper,CategoricalColorMapper,LinearColorMapper
from bokeh.plotting import figure

data = pd.read_csv("http://www.football-data.co.uk/mmz4281/1516/I1.csv")

Team1 = list(data.iloc[range(0,10,1),:].HomeTeam)
Team2 = list(data.iloc[range(0,10,1),:].AwayTeam)
Team = Team1+Team2
Team.sort()

zero = np.zeros((20,38))
D = pd.DataFrame(zero)
DD = pd.DataFrame(np.array(Team).reshape(20,1))
DD.columns=['Team']
D = pd.concat([D,DD],axis=1)
D = D.set_index('Team')
D.columns=[str(i) for i in np.arange(1,39)]

data2 = data.iloc[range(0,380,1),[1,2,3,4,5,6]]
data2['Hdiff']=data2['FTHG']-data2['FTAG']
data2['Adiff']=data2['FTAG']-data2['FTHG']

for i in range(data2.shape[0]):
    col = int(i/10)
    D.iloc[D.index==data2.HomeTeam[i],col] = data2.Hdiff[i]
    D.iloc[D.index==data2.AwayTeam[i],col] = data2.Adiff[i]

Rounds = list(D.columns.values)
Teams = [str(i) for i in D.index]

# Set up the data for plotting. We will need to have values for every
# pair of rounds/teams names. Map the rate to a color.
Team = []
Round = []
Color = []
Difference = []
for r in Rounds:
    for t in Teams:
        Team.append(t)
        Round.append(r)
        d = np.array(D.iloc[D.index==t,D.columns.values==r])
        Difference.append(d[0][0])

# this is the colormap from the original NYTimes plot
colors = ["#75968f", "#a5bab7", "#c9d9d3", "#dfccce", "#e2e2e2", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
colors2 = ['#5d7872','#82a09a','#75968f','#bacac7','#d5dfdd',
      '#f1f4f3','#ccb5bb','#aa858e','#885460','#763b4a','#662333']
colors3 = ['#3a6051', '#4e806c', '#62a188','#81b39f', '#a0c6b7','#c0d9cf', 
          '#dfece7',
          '#bb9da4','#996c77','#763b4a','#550b1d','#440817','#330611']
colors4 = ['#3a6051', '#4e806c','#4e806c','#4e806c','#4e806c','#4e806c',
          '#4e806c','#4e806c','#4e806c','#4e806c','#4e806c','#4e806c','#4e806c','#4e806c','#dfece7']
#mapper = LinearColorMapper(palette=colors3)
mapper = CategoricalColorMapper(palette=colors3,factors=range(-6,7,1))

source = ColumnDataSource(data=dict(Team=Team, Round=Round, Difference=Difference, 
                          Difference_Real=Difference))

TOOLS = "hover,save,pan,box_zoom,wheel_zoom"

p = figure(title="2015-2016 Serie A",
           x_range=Rounds, y_range=list(reversed(Teams)),
           x_axis_location="above", plot_width=900, plot_height=400,
           tools=TOOLS)
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "8pt"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = pi / 3

p.rect(x="Round", y="Team", width=1, height=1,
       source=source,
       fill_color={'field': 'Difference', 'transform': mapper},
       line_color=None)

p.select_one(HoverTool).tooltips = [
    ('Info', '@Team @Round'),
    ('Goal Difference', '@Difference_Real'),
]

#output_file("heatmap.html", title="heatmap.py example")

show(p)