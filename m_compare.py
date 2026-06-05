#!/usr/bin/env python3

'''
This script creates a mean forecast by averaging the max db_h/dt values in a
twenty minutes time intervalfrom the five models used in Pulkkinen et al. 2013.
Plots comparison of model performance of all five models and the mean, median, and observatios.
Used as figure 1 in the paper.
'''

import numpy as np
import multimodtools as mmt
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from spacepy.plot import applySmartTimeTicks

from argparse import ArgumentParser

parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--events", type=int, nargs='+',
                    default=[1],
                    help="Set the events to analyze via list of event number,"
                    + "e.g., --events 1 2 7 8")
parser.add_argument("-m", "--mag", type=str, default='YKC',
                    help='Set the magnetometer to analyze: ABK, PBQ, ' +
                    'SNK, YKC, NEW, OTT, or WNG')

# Process arguments
args = parser.parse_args()

# Set station names:
names = {'ABK': 'Abisko', 'PBQ': 'Poste de la Baleine', 'SNK': 'Sanikiluaq',
         'YKC': 'Yellowknife', 'NEW': 'Newport', 'OTT': 'Ottowa',
         'WNG': 'Wingst'}

# Set plot style:
try:
    plt.style.use('seaborn')
except OSError:
    plt.style.use('seaborn-v0_8')

# script options into function arguments?
tab_kwargs = {'event_set': args.events, 'mag_set': args.mag, 'verbose': False}

# Create mean forecast
# Loop over all models
t = {}
for m in mmt.models:
    t[m] = mmt.build_table(m, **tab_kwargs)

# Get time array into convenience variable:
plottime = t['9_SWMF'].time

# calculate mean
modmean = np.zeros(plottime.size)
for m in mmt.models:
    modmean += t[m].modmax
modmean /= 5

# Create median forecast
# Loop over all models
t = {}
for m in mmt.models:
    t[m] = mmt.build_table(m, **tab_kwargs)

# Get time array into convenience variable:
plottime = t['9_SWMF'].time
modmedian = np.zeros(plottime.size)

# Stack and calculate medians
modmedian = np.vstack([t['9_SWMF'].modmax, t['2_LFM-MIX'].modmax, t[
    '4_OPENGGCM'].modmax, t['6_WEIMER'].modmax, t['3_WEIGEL'].modmax])
modmedian = np.median(modmedian, axis=0)

# TOP PLOT:
fig = plt.figure(figsize=(10, 7), layout='constrained')
a1, a2 = fig.subplots(2, 1, sharex=True)

fig.suptitle(f"Event {tab_kwargs['event_set'][0]} - " +
             f"{names[tab_kwargs['mag_set']]}", fontsize=20)

# First plot: validation plot - each models max compared to ensemble mean
for mod in mmt.modnames:
    a1.plot(plottime, t[mod].modmax, c=mmt.cols[mod],
            label=mmt.models[mod], alpha=0.75)
a1.plot(plottime, modmean, c='black', ls='--', label='Ensemble Mean', lw=3.5)
a1.plot(plottime, modmedian, c='grey', ls='--', label='Ensemble Median', lw=3.5)

# BOTTOM PLOT:
a2.plot(plottime, t['9_SWMF'].modmax, '-*', c='royalblue', label='SWMF',
        alpha=0.85)
a2.plot(plottime, t['9_SWMF'].obsmax, '-X', c='crimson', label='Observations',
        alpha=0.85)
a2.plot(plottime, modmean, '-s', c='black', label='Ensemble Mean')
a2.plot(plottime, modmedian, '--o', c='grey', label='Ensemble Median')

# Set plot subtitles:
a1.text(0.01, 0.93, 'Ensemble Members', fontsize=16, transform=a1.transAxes)
a2.text(0.01, 0.93, 'Ensemble Forecasts', fontsize=16, transform=a2.transAxes)

# Touch up axes:
for ax in (a1, a2):
    ax.set_ylabel('$dB_H/dt$ ($nT$)', fontsize=16)
    ax.legend(loc='upper right', edgecolor='white', framealpha=1)
    yrange = ax.get_ylim()
    mult = 2 if yrange[1] - yrange[0] < 5 else 5
    ax.yaxis.set_major_locator(MultipleLocator(mult))
    ax.tick_params(axis='both', labelsize=15)
applySmartTimeTicks(a2, plottime, dolabel=True)

plt.show()