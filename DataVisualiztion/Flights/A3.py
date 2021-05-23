# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:37:17 2020

@author: 54963
"""

import numpy as np 
import pandas as pd 

import plotly as py
import plotly.express as px

import plotly.graph_objects as go

import matplotlib.pyplot as plt


#from plotly.offline import iplot, plot, init_notebook_mode


# 加载数据
flight = pd.read_csv('Flights dataset.csv')

# timesData相关信息
#flight.info()

flight.head()

fig = px.parallel_categories(flight)
fig.show()