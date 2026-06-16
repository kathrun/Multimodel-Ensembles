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

# Plot all that data!
mmt.set_plot_params()
labels = {'hss': r'$\Delta$HSS', 'pod': r'$\Delta$PoD',
          'pofd': r'$\Delta$PoFD', 'bias': 'Bias'}

fig = plt.figure(figsize=(13.6, 10))
row1, row2, row3, row4 = fig.subplots(4, 4, sharex=True)
# (a1, a2, a3, a4), (b1, b2, b3, b4), (c1, c2, c3, c4), (d1, d2, d3, d4) = \
#    fig.subplots(4, 4, sharex=True)

for tnow, row in zip(thresh, (row1, row2, row3, row4)):
    # Get string version of our threshold:
    str_t = f"{10*tnow:02.0f}"
    print(f"Working on threshold = {str_t}")

    pofd_all = (np.array(mme_all['pofd03']) - detm['pofd'][0])
    pofd_hi = (np.array(mme_hi['pofd03']) - detm['pofd'][0])
    pofd_lo = (np.array(mme_lo['pofd03']) - detm['pofd'][0])

    hss_all = np.array(mme_all['hss03']) - detm['hss'][0]
    hss_hi = np.array(mme_hi['hss03']) - detm['hss'][0]
    hss_lo = np.array(mme_lo['hss03']) - detm['hss'][0]

    for ax, met in zip(row, ('pod', 'pofd', 'hss', 'bias')):

        # Set labels:
        if row is row1:
            ax.set_title(f'{labels[met]}')
        ax.set_ylabel(f"{tnow:.1f}$nT/s$\nThreshold")
        ax.set_xlabel('$N$ NPCs')
        ax.label_outer(True)

        # Calculate difference in metrics:
        met_all = np.array(mme_all[met+str_t]) - detm[met][0]
        met_hi = np.array(mme_hi[met+str_t]) - detm[met][0]
        met_lo = np.array(mme_lo[met+str_t]) - detm[met][0]

        ax.plot(npc, met_all, '-C1', marker='o')
        ax.plot(npc, met_hi, '-C0', marker='o')
        ax.plot(npc, met_lo, '-C2', marker='o')

fig.tight_layout()
plt.show()