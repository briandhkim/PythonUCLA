# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 18:31:17 2017

@author: Brian
"""

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

py.sign_in('w1057216', 'e6m3sexk0v')


data = py.get_figure("https://plot.ly/~dfreder1/69/").get_data()

fontDict = dict(family = 'Times New Roman', size = 12, color = 'black')

layout = go.Layout(title='Total Bridges Built in CA Since 1900', titlefont = fontDict,width =600, height = 400,xaxis = dict(title = 'Year', titlefont = fontDict,
                                 showticklabels = True, tickfont = fontDict, ticks = 'outside', 
                                 range = [1900,2013], dtick = 10, tickwidth = 1),
                                 yaxis = dict(title = 'Total Bridges', titlefont = fontDict, showticklabels = True,
                                              tickfont = fontDict, ticks = 'outside', tick0 = 0, dtick = 5000, 
                                              tickwidth = 1))

df = pd.Series(data)    #contain plotly data into Series from pandas

df.loc[0]['x']          #the values were contained in var 'x'
x = []
x = df.loc[0]['x']      #the values (list of years) stored in a list

yrs = {}                #finding duplicate years to count bridges
for i in x:
    yrs[i] = x.count(i)

list(yrs) 
list(yrs.values())   

list_key = []
list_val = []
list_key = list(yrs)

for x in list_key:              #removing any years or other keys not matching 1900-present years
    if x < 1900 or x > 2015:
        yrs.pop(x,None)
        
list_key = list(yrs)
list_val = list(yrs.values())

list_val_cumu = []                  #cumulative sum of the bridges built 
list_val_cumu = np.cumsum(list_val)

trace0 = go.Scatter(x=list_key, y=list_val_cumu, mode = 'lines',
                    line=dict(width=1.5, color = 'rgb(255,165,0)'), fill = 'tonexty')
data = [trace0]
fig = go.Figure(data = data, layout = layout)
py.plot(fig, filename = 'BridgesInCA')
py.image.save_as(fig, 'CAbridges.png', scale = 3) #save as png with scale 3 which multiplies the w and h by 3
