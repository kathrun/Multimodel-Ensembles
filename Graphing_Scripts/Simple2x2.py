# Creates a plot to show the changes in NPC performance across all metrics for
# a single threshold.
'''
Requires run analysis_scripts/gen_npc_mets.py
'''

import os
import pickle

import numpy as np
import multimodtools as mmt
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Open the pickles for all three mag sets
metfile = 'npc_metrics_mags_all.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/npc_metrics_mags_all.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled all mags data.'
                            'See docstring.')

with open('npc_metrics_mags_all.pkl', 'rb') as f:
    mme_all = pickle.load(f)

metfile = 'npc_metrics_mags_hi.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/npc_metrics_mags_hi.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled hi mags data. See docstring.')

with open('npc_metrics_mags_hi.pkl', 'rb') as f:
    mme_hi = pickle.load(f)

metfile = 'npc_metrics_mags_lo.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/npc_metrics_mags_lo.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled lo mags data. See docstring.')

with open('npc_metrics_mags_lo.pkl', 'rb') as f:
    mme_lo = pickle.load(f)

metfile = 'mean_metrics.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/mean_metrics.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled deterministic data. '
                            'See docstring for halp')

with open('mean_metrics.pkl', 'rb') as f:
    detm, mean, medi = pickle.load(f)

# Grab data from pickle
npc = mme_all['n_members']
thresh = detm['thresh']

# Grab deterministc and calculate difference for PoD, PoFD, and HSS.
pod_all = np.array(mme_all['pod03']) - detm['pod'][0]
pod_hi = np.array(mme_hi['pod03']) - detm['pod'][0]
pod_lo = np.array(mme_lo['pod03']) - detm['pod'][0]

pofd_all = (np.array(mme_all['pofd03']) - detm['pofd'][0])*(-1)
pofd_hi = (np.array(mme_hi['pofd03']) - detm['pofd'][0])*(-1)
pofd_lo = (np.array(mme_lo['pofd03']) - detm['pofd'][0])*(-1)

hss_all = np.array(mme_all['hss03']) - detm['hss'][0]
hss_hi = np.array(mme_hi['hss03']) - detm['hss'][0]
hss_lo = np.array(mme_lo['hss03']) - detm['hss'][0]

# Make those plots!

# Create the difference between determ and MME performance.
# set style information
mmt.set_plot_params()

# creating subplots
fig = plt.figure(figsize=(11.82,  7.12))
(a1, a2), (a3, a4) = fig.subplots(2, 2, sharex=True)

fig.suptitle('0.3nT/s Threshold', fontsize=24)

# PoD
# set labels and titles
a1.set_ylabel('$\Delta$PoD')
a1.xaxis.set_major_locator(ticker.MultipleLocator(1))

# plot mag groups
a1.plot(npc, pod_all, 'C1', marker='o', label='All')
a1.plot(npc, pod_hi, '-C0', marker='o', label='High')
a1.plot(npc, pod_lo, '-C2', marker='o', label='Low')

# PoFD
# set labels and titles
a2.set_ylabel('-$\Delta$PoFD')

# plot mag groups
a2.plot(npc, pofd_all, '-C1', marker='o')
a2.plot(npc, pofd_hi, '-C0', marker='o')
a2.plot(npc, pofd_lo, '-C2', marker='o')

# HSS
# set labels and titles
a3.set_ylabel('$\Delta$HSS')
a3.set_xlabel('$N$ NPCs')

# plot mag groups
a3.plot(npc, hss_all, '-C1', marker='o')
a3.plot(npc, hss_hi, '-C0', marker='o')
a3.plot(npc, hss_lo, '-C2', marker='o')

# set labels and titles
a4.set_ylabel('Bias')
a4.set_xlabel('$N$ NPCs')
a4.axhline(y=1, color='grey', linestyle="--")

# plot mag groups
a4.plot(npc, mme_all['bias03'], '-C1', marker='o')
a4.plot(npc, mme_hi['bias03'], '-C0', marker='o')
a4.plot(npc, mme_lo['bias03'], '-C2', marker='o')

# legend
a1.legend(loc='upper right', edgecolor='white', framealpha=1,
          title='Magnetometers', title_fontsize=18, fontsize=15)

plt.show()
