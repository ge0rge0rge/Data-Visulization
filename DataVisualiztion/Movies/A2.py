# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:08:23 2020

@author: 54963
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import seaborn as sns
import numpy as np

#%matplotlib inline

#read dataset
movies = pd.read_csv('movies.csv')
movies.head()


cols = ['Production Budget','IMDB Rating','Rotten Tomatoes Rating',
        'IMDB Votes', 'Major Genre']
pp = sns.pairplot(movies[cols],hue = 'Major Genre', height=1.8, aspect=1.8,                 
                  plot_kws=dict(edgecolor="k", linewidth=0.5),
                  diag_kind="kde", diag_kws=dict(shade=True))

fig = pp.fig 
fig.subplots_adjust(top=0.93, wspace=0.3)
t = fig.suptitle('Movies\' Production Budget - Reviews Plots', fontsize=14)
plt.show()


cols = ['Production Budget','IMDB Rating','Rotten Tomatoes Rating',
        'IMDB Votes']
subset_df = movies[cols]

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
scaled_df = ss.fit_transform(subset_df)
scaled_df = pd.DataFrame(scaled_df, columns=cols)
final_df = pd.concat([scaled_df, movies['Major Genre']], axis=1)
final_df.head()

from pandas.plotting import parallel_coordinates
pc = parallel_coordinates(final_df, 'Major Genre', color = ('#FFE888', '#FF9999'))                                                        
plt.show()