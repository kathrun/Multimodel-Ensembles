#/usr/bin/env python3
'''
Let's build a proof-of-concept multi-model ensemble forecast using
naive probabilistic classifiers.

We'll use Event 7 NEW and YKC as examples, then build a full metric suite.
'''

import numpy as np
import matplotlib.pyplot as plt

from spacepy.plot import style, applySmartTimeTicks
from validator import BinaryEventTable
import multimodtools as mmt

style()

# Set metric parameters:
mag, event, thresh = 'WNG', 4, 0.3
tab_kwargs = {'event_set':[event], 'mag_set':[mag], 'thresh':thresh}

# Create tables for all 5 models.
tables = {}
for m in mmt.models:
    tables[mmt.models[m]] = mmt.build_table(m, **tab_kwargs)


# Create NPC by counting the number of crossings in each bin
# across all ensemble members (i.e., models)
mod = np.zeros(tables['SWMF'].obsmax.size)
for tab in tables:
    mod += 1*tables[tab].bool

npc_forecast = 1.1 * thresh * (mod>=2)
npc_tab = BinaryEventTable(tables['SWMF'].tObs, tables['SWMF'].Obs, tables['SWMF'].time, 
                           npc_forecast, thresh, trange=mmt.tlims[event], window=20*60)

# Create a cool plot:
fig = plt.figure(figsize=(10,7))
a1, a2 = fig.subplots(2,1)

# Top fig: Ensemble forecast mess
for m in tables:
    a1.plot(tables[m].tMod, tables[m].Mod, c='C0', alpha=0.5)
a1.plot(tables['SWMF'].tObs, tables['SWMF'].Obs, c='crimson', label='Obs.')
a1.plot(tables['SWMF'].time, tables['SWMF'].obsmax, 'x', c='crimson')


# Center fig: Bin maxes
for m in tables:
    a2.plot(tables[m].time, tables[m].modmax, 'o', c='C0', alpha=0.5, ms=5,
            label='Ensemble' if m == 'SWMF' else '_')
a2.plot(tables['SWMF'].time, tables['SWMF'].obsmax,
        'x', c='crimson', label='Obs.')
a2.plot(tables['SWMF'].tObs, tables['SWMF'].Obs, c='crimson')
a2.plot(tables['SWMF'].time, tables['SWMF'].modmax, '*', c='gold', label='SWMF')
a2.legend(loc='best')

a1.set_title(f"Multi-Model Forecast: {tab_kwargs['mag_set'][0]}")
for ax in (a1, a2):
    applySmartTimeTicks(ax, mmt.tlims[tab_kwargs['event_set'][0]],
                        dolabel=ax is a2)
    ax.set_ylabel(r'$|\frac{dB_H}{dt}|$ ($nT/s$)')
    ax.hlines(tab_kwargs['thresh'], *mmt.tlims[tab_kwargs['event_set'][0]],
              linestyles='dashed', colors='k')

fig.tight_layout()
thresh_str = f"{tab_kwargs['thresh']}".replace('.','p')
fig.savefig(f"./multi_model_event{tab_kwargs['event_set'][0]}_mag{tab_kwargs['mag_set'][0]}_thresh{thresh_str}.png")

# Now, make some sweet sweet metrics.
swmf = tables['SWMF']
print(f'Station: {mag}\tEvent: {event}\tThreshold: {thresh}')
print(f'Deterministic Forecast:\n\tPoD = {swmf.calc_HR()}\n\tPoFD = {swmf.calc_FARate()} \n\tHSS = {swmf.calc_heidke()}\n\tBias = {swmf.calc_bias()}')
print(f'Ensemble Forecast:\n\tPoD = {npc_tab.calc_HR()}\n\tPoFD = {npc_tab.calc_FARate()} \n\tHSS = {npc_tab.calc_heidke()}\n\tBias = {npc_tab.calc_bias()}')