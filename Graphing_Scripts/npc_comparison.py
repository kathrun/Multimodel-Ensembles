#/usr/bin/env python3
'''
Trying to recreate single magnetometer model comparison graph. 
'''

import numpy as np
import matplotlib.pyplot as plt

from spacepy.plot import style, applySmartTimeTicks
from validator import BinaryEventTable
import multimodtools as mmt

import os, sys
from datetime import datetime, timedelta
from argparse import ArgumentParser

parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--event", type=int, nargs='+',
                    default= 4,
                    help="Set the event to analyze from the event list:" +
                    "1, 2, 3, 4, 7, 8 ")
parser.add_argument("-d", "--debug", action="store_true",
                    help="Turn on debug mode: additional print statements, " +
                    "output saved in 'debug/' folder")
parser.add_argument("-t", "--threshold", type=float, default=0.3,
                    help="Set the threshold for dB/dt in the binary event" +
                    "analysis. Default is 0.3, standard values are " +
                    "0.3, 0.7, 1.1, and 1.5 nT/s.")
parser.add_argument("-n", "--n_models", type=int, default=2,
                    help="Set the number of models that must cross the dB/dt " +
                    "threshold in order for the NPC prediction to be counted " +
                    "as a 'hit'. Defaults to 2.")
parser.add_argument("-m", "--mag", type=str, default='YKC',
                    help='Set the magnetometer to analyze: ABK, PBQ, ' +
                    'SNK, YKC, NEW, OTT, or WNG')

# Process arguments:
args = parser.parse_args()

tab_kwargs = {'event_set': args.event, 'mag_set': args.mag,
              'thresh': args.threshold, 'verbose': False}

# Create tables for all 5 models.
t = {}
for m in mmt.models:
    t[m] = mmt.build_table(m, **tab_kwargs)

# Time for convience.
time = t['9_SWMF'].time

# Create NPC by counting the number of crossings in each bin
# across all ensemble members (i.e., models)
mod = np.zeros(t['9_SWMF'].obsmax.size)
for tab in t:
    mod += 1*t[tab].bool

npc_forecast = 1.1 * args.threshold * (mod >= 2)
npc_tab = BinaryEventTable(t['9_SWMF'].tObs, t['9_SWMF'].Obs, t['9_SWMF'].time,
                           npc_forecast, args.threshold,
                           trange=mmt.tlims[args.event], window=20*60)

# Plotting
fig = plt.figure(figsize=(10, 7))
a1, a2 = fig.subplots(2, 1)

for mod in mmt.modnames:
    a1.plot(time, t[mod].modmax, c=mmt.cols[mod],
            label=mmt.models[mod], alpha=0.75)
a1.plot(time, t['9_SWMF'].obsmax, '-', c='black', label='Observations')
a1.axhline(y=args.threshold, linestyle='dashed', c='grey', label="Threshold")
a1.legend(loc='best')

# Center fig: Bin maxes
# PLOT NPC > 2 (try all npc?)
a2.plot(time, npc_tab.modmax, '-o', c='crimson', label='NPC Forecast')
a2.plot(time, t['9_SWMF'].obsmax, '-x', c='black', label='Observations')
a2.plot(time, t['9_SWMF'].modmax, '-*', c='royalblue', label='SWMF')
a2.axhline(y=args.threshold, linestyle='dashed', c='grey', label="Threshold")
a2.legend(loc='best')

a1.set_title(f"Multi-Model Forecast: {tab_kwargs['mag_set']}")
for ax in (a1, a2):
    ax.set_ylabel(r'$|\frac{dB_H}{dt}|$ ($nT/s$)')

fig.tight_layout()
plt.show()