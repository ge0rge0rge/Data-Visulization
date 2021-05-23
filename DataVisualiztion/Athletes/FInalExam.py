import csv

import numpy as np
import pandas as pd

import plotly as py
import plotly.express as px
import plotly.graph_objects as go

import matplotlib.pyplot as plt

################
# read dataset #
################
df = pd.read_csv('athlete_events.csv', encoding='utf-8')
df1 = pd.read_csv('athlete_events.csv', encoding='utf-8')
# df.info()
# print(df.head(10))

#################################
# sort & fill nan & save dataset #
#################################
data = df[df['Medal'].notna()]
data.to_csv('athlete_sorted.csv', na_rep='0')
df = pd.read_csv('athlete_sorted.csv', encoding='utf-8')

df1.to_csv('athlete_sorted1.csv', na_rep='N')
df1 = pd.read_csv('athlete_sorted1.csv', encoding='utf-8')
# values = {'Age': 1}
# df = df.fillna(value=values)

# df.info()
# print(df.head(10))


##################
# Physical fitness #
##################
fig = px.scatter(df, x="Height", y="Weight", color="Medal", symbol='Sex', size='Age')
fig.show()

############
# Location #
############
fig = px.histogram(df, x="City", color="Medal")
fig.show()

fig = px.histogram(df1, x="City", color="Medal")
fig.show()
##################
# Time #
##################
fig = px.density_heatmap(df, x="Year", y="Season", facet_row="Sex", facet_col="Medal")
fig.show()

###########
# OverAll #
###########
fig = px.scatter_3d(df, x='Year', y='Height', z='Weight',
                    color='Medal', symbol='Season', size='Age')
fig.show()