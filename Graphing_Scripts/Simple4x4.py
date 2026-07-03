'''
Requires run analysis_scripts/gen_npc_mets.py
'''
# Incomplete! Either update pickels or try looping,

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
    mme_all, best_all = pickle.load(f)

metfile = 'npc_metrics_mags_hi.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/npc_metrics_mags_hi.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled hi mags data. See docstring.')

with open('npc_metrics_mags_hi.pkl', 'rb') as f:
    mme_hi, best_hi = pickle.load(f)

metfile = 'npc_metrics_mags_lo.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/npc_metrics_mags_lo.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled lo mags data. See docstring.')

with open('npc_metrics_mags_lo.pkl', 'rb') as f:
    mme_lo, best_lo = pickle.load(f)

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

# Plot all that data!
mmt.set_plot_params()
labels = {'hss': r'$\Delta$HSS', 'pod': r'$\Delta$PoD',
          'pofd': r'$\Delta$PoFD', 'bias': 'Bias'}

fig = plt.figure(1, figsize=(13.6, 10))
fig.suptitle('Simple NPC', fontsize=24)
fig.subplots_adjust(wspace=0.025, hspace=0.05)
row1, row2, row3, row4 = fig.subplots(4, 4)
for ithresh, (tnow, row) in enumerate(zip(thresh, (row1, row2, row3, row4))):
    # Get string version of our threshold:
    str_t = f"{10*tnow:02.0f}"
    print(f"Working on NPC threshold = {str_t}")

    for ax, met in zip(row, ('pod', 'pofd', 'hss', 'bias')):

        # Set labels:
        if row is row1:
            ax.set_title(f'{labels[met]}')
        ax.set_ylabel(f"{tnow:.1f} $nT/s$\nThreshold")
        ax.set_xlabel('$N$ NPCs')
        ax.label_outer(True)

        if met != 'bias':
            met_all = np.array(mme_all[met+str_t]) - detm[met][ithresh]
            met_hi = np.array(mme_hi[met+str_t]) - detm[met][ithresh]
            met_lo = np.array(mme_lo[met+str_t]) - detm[met][ithresh]
            
            ax.plot(npc, met_all, '-C1', marker='o')
            ax.plot(npc, met_hi, '-C0', marker='o')
            ax.plot(npc, met_lo, '-C2', marker='o')
        else:
            ax.plot(npc, mme_all['bias'+str_t], '-C1', marker='o')
            ax.plot(npc, mme_hi['bias'+str_t], '-C0', marker='o')
            ax.plot(npc, mme_lo['bias'+str_t], '-C2', marker='o')

        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))


fig.legend(["All Mags", "High Mags", 'Low Mags'], loc="lower center",
           bbox_to_anchor=(0.5, 0.0), ncols=3, fontsize=15)

# fig.tight_layout()
plt.savefig('WIP_simple.png')


# Best of figure
fig = plt.figure(2, figsize=(13.6, 10))
fig.subplots_adjust(wspace=0.025, hspace=0.05)
fig.suptitle('Best of NPC', fontsize=24)
row1, row2, row3, row4 = fig.subplots(4, 4, sharex=True)
for ithresh, (tnow, row) in enumerate(zip(thresh, (row1, row2, row3, row4))):
    # Get string version of our threshold:
    str_t = f"{10*tnow:02.0f}"
    print(f"Working on Best NPC threshold = {str_t}")

    for ax, met in zip(row, ('pod', 'pofd', 'hss', 'bias')):

        # Set labels:
        if row is row1:
            ax.set_title(f'{labels[met]}')
        ax.set_ylabel(f"{tnow:.1f} $nT/s$\nThreshold")
        ax.set_xlabel('$N$ NPCs')
        ax.label_outer(True)

        if met != 'bias':
            met_all = np.array(best_all[met+str_t]) - detm[met][ithresh]
            met_hi = np.array(best_hi[met+str_t]) - detm[met][ithresh]
            met_lo = np.array(best_lo[met+str_t]) - detm[met][ithresh]
            
            ax.plot(npc, met_all, '-C1', marker='o')
            ax.plot(npc, met_hi, '-C0', marker='o')
            ax.plot(npc, met_lo, '-C2', marker='o')

        else:
            ax.plot(npc, best_all['bias'+str_t], '-C1', marker='o')
            ax.plot(npc, best_hi['bias'+str_t], '-C0', marker='o')
            ax.plot(npc, best_lo['bias'+str_t], '-C2', marker='o')

        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

fig.legend(["All Mags", "High Mags", 'Low Mags'], loc="lower center", ncols=3,
           fontsize=15)

plt.savefig('WIP_best.png')

plt.show()
