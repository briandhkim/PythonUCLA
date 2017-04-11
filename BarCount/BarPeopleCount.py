# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 18:36:22 2017

@author: Brian

this was designed to determine the average number of customers at a pub at a given hour
    based on raw data distributed over 100 separate CSV files. The time was divided into 20 minute intervals
"""

import os
import pandas as pd
import numpy as np

def round_time(nums):          #function for rounding time down to 20 mins 
    time = div * (nums//div)
    return time

def process_file(filename):
    reader = pd.read_csv(filename, names = ['time', 'inst', 'cumu']) 
                                                            #read a single csv file (without setting time as the index into a DataFrame and assign names to the columns)
    
    reader = reader.dropna(thresh=2)    #drops nan values
    
    #tNum = reader.loc[0:0,['time']] #grabs the first time of the table
    reader.loc [0:0,['time']] = round_time(reader.loc[0:0,['time']])    #step 3**********
    reader = reader.set_index('time')       #step 4**************************************
    reader.index = pd.to_datetime(reader.index, unit = 'ms', utc = True)    #step 5******
                #have to set it equal to .index; need to specify unit to 'ms' milisec
    reader.index = reader.index.tz_convert('US/Eastern')    #step 6**********************
    reader = reader.asfreq('20Min', method = 'pad')     #step 7**************************
    reader['TOD'] = reader.index.strftime('%A %H:%M')   #step 8**************************
    
    return reader
    
dirPath =  r'' #will need user specific directory path
files = os.listdir(dirPath)
csvFile = [] 
for f in files:
    if f.endswith('.csv'):
        csvFile.append(f)

data = []
df = pd.DataFrame()
for f in csvFile:
    data.append(process_file(f))
    
df = pd.concat(data)
df = df.groupby('TOD').mean()
print df
label = [ 'inst']
df.to_csv(r'output.txt', columns = label)
df.to_excel(r'output.xlsx', columns = label)