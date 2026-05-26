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

import matplotlib.pyplot as plt

plt.style.use('seaborn')

metfile = 'mean_metrics.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/mean_metrics.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled data. See docstring for halp')

with open('mean_metrics.pkl', 'rb') as f:
    detm, mean, medi = pickle.load()
