#!/usr/bin/env python3

'''
Create Figure 2: comparison of deterministic/mean/median forecasts for all
thresholds and metrics.

Requires that you run gen_meanmed_mets.py from the top-level folder (i.e.,
`run analysis_scripts/gen_meanmed_mets.py` has been called and
`mean_metrics.pkl` exists.)
'''

import os
import pickle

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

metfile = 'mean_metrics.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/mean_metrics.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled data. See docstring for halp')

with open('mean_metrics.pkl', 'rb') as f:
    detm, mean, medi = pickle.load(f)

#Graph the pickle
# Get the threshold from the file.
thresh = detm['thresh']  #  0.3, 0.7, 1.1, 1.5
# set style information
plt.style.use('seaborn')


# creating subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout='constrained', figsize=(10,8))
fig.suptitle('Mean vs Median Comparison', fontsize=33)

# Start with POD figure.
ax1.plot(thresh, detm['pod'], label='SWMF/Deterministic')
ax1.plot(thresh, medi['pod'], label='Median')
ax1.plot(thresh, mean['pod'], label='Mean')

#PoFD figure
ax2.plot(thresh, detm['pofd'], label='SWMF/Deterministic')
ax2.plot(thresh, medi['pofd'], label='Median')
ax2.plot(thresh, mean['pofd'], label='Mean')

#HSS figure
ax3.plot(thresh, detm['hss'], label='SWMF/Deterministic')
ax3.plot(thresh, medi['hss'], label='Median')
ax3.plot(thresh, mean['hss'], label='Mean')

#Bias 
ax4.plot(thresh, detm['bias'], label='SWMF/Deterministic')
ax4.plot(thresh, medi['bias'], label='Median')
ax4.plot(thresh, mean['bias'], label='Mean')

plt.show()

#To-do
#fix labels, ticks, fonts, and line style and color to be consistent with paper figures
#add legend, x,y labels, and subtitles 