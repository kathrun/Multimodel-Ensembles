# Creates a plot to show the changes in NPC performance across all metrics for
# a single threshold.
'''
Requires run analysis_scripts/gen_npc_mets.py
'''

import os
import pickle

import numpy as np
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
plt.style.use('seaborn')

# creating subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout='constrained',
                                             figsize=(10, 8), sharex=True)
plt.tick_params(axis='y', labelsize=15)

fig.suptitle('0.3nT/s Threshold', fontsize=30)

# PoD
# set labels and titles
ax1.set_ylabel('$\Delta$PoD', fontsize=24)
ax1.yaxis.set_tick_params(labelsize=20)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))

# plot mag groups
ax1.plot(npc, pod_all, 'C1', marker='o', markersize='10', linewidth=5)
ax1.plot(npc, pod_hi, '-C0', marker='o', markersize='10', linewidth=5)
ax1.plot(npc, pod_lo, '-C2', marker='o', markersize='10', linewidth=5)

# PoFD
# set labels and titles
ax2.set_ylabel('-$\Delta$PoFD', fontsize=24)
#ax2.yaxis.set_tick_params(labelsize=20)

# plot mag groups
ax2.plot(npc, pofd_all, 'C1', marker='o', markersize='10', linewidth=5)
ax2.plot(npc, pofd_hi, '-C0', label='High', marker='o', markersize='10',
         linewidth=5)
ax2.plot(npc, pofd_lo, '-C2', label="Low", marker='o', markersize='10',
         linewidth=5)

# HSS
# set labels and titles
ax3.set_ylabel('$\Delta$HSS', fontsize=24)
ax3.set_xlabel('$N$ NPCs', fontsize=24)
ax3.xaxis.set_tick_params(labelsize=20)
ax3.yaxis.set_tick_params(labelsize=20)

# plot mag groups
ax3.plot(npc, hss_all, 'C1', marker='o', markersize='10', linewidth=5)
ax3.plot(npc, hss_hi, '-C0', marker='o', markersize='10', linewidth=5)
ax3.plot(npc, hss_lo, '-C2', marker='o', markersize='10', linewidth=5)

# set labels and titles
ax4.set_ylabel('Bias', fontsize=24)
ax4.set_xlabel('$N$ NPCs', fontsize=24)
ax4.xaxis.set_tick_params(labelsize=20)
ax4.yaxis.set_tick_params(labelsize=20)
ax4.axhline(y=1, color='grey', linestyle="--")

# plot mag groups
ax4.plot(npc, mme_all['bias03'], '-C1', label='All', marker='o',
         markersize='10', linewidth=5)
ax4.plot(npc, mme_hi['bias03'], '-C0', label='High', marker='o',
         markersize='10', linewidth=5)
ax4.plot(npc, mme_lo['bias03'], '-C2', label="Low", marker='o',
         markersize='10', linewidth=5)

# legend
ax4.legend(loc='upper right', edgecolor='white', framealpha=1,
           title='Magnetometers', title_fontsize=18, fontsize=15)

plt.show()
