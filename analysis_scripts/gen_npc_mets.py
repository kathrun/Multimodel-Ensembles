#!/usr/bin/env python3

'''
Top level script to create metrics for all NPC values to create graphs in
following figures ...

It creates PoD/PoFD/HSS/Bias for the deterministic and NPC 1-5.
The result is saved as a Python pickle for use in future analysis.

Results are saved as "npc_metrics.pkl" and can be opened with the following:

```
import pickle
with open('npc_metrics.pkl', 'rb') as f:
    npc = pickle.load()
```
'''
# Goal: Save all simple NPC metrics in a pickle for all NPC, all events, all
# mag groups, and all threshold
# for recreatability and uniform graphs

import pickle

from datetime import datetime, timedelta

import numpy as np

from validator import BinaryEventTable
import multimodtools as mmt

npc = [1, 2, 3, 4, 5]

# Create tables for all 5 models.
tables = {}
for m in mmt.models:
    print([m])
    tables[mmt.models[m]] = mmt.build_table(m, event_set='all', mag_set='all')

# create tables for all npc.
npc_tab = {}

# Setting up tables
npc_size, obs_size = tables['SWMF'].obsmax.size, tables['SWMF'].Obs
tstart = datetime(2000, 1, 1, 0, 0, 0)
t_npc = [tstart + timedelta(minutes=i*20 + 10) for i in range(npc_size)]
t_npc = np.array(t_npc)

# Deterministic model data to the pickle
# detm = {}
# for v in ['pod', 'pofd', 'hss', 'bias']:
#     detm[v] = []
#     detm['pod'].append(npc_tab.calc_HR())
#     detm['pofd'].append(npc_tab.calc_FARate())
#     detm['hss'].append(npc_tab.calc_heidke())
#     detm['bias'].append(npc_tab.calc_bias())

# Creating NPC tables
for n in npc:
    mod = np.zeros(tables['SWMF'].obsmax.size)
    for tab in tables:
        mod += 1*tables[tab].bool

    npc_forecast = 1.1 * 0.3 * (mod >= [n])
    npc_tab = BinaryEventTable(t_npc, tables['SWMF'].obsmax,
                               t_npc, npc_forecast, 0.3,
                               window=20*60, verbose=False)

    mme = {'NPC': npc}
    for v in ['pod', 'pofd', 'hss', 'bias']:
        mme[v] = []
    mme['pod'].append(npc_tab.calc_HR())
    mme['pofd'].append(npc_tab.calc_FARate())
    mme['hss'].append(npc_tab.calc_heidke())
    mme['bias'].append(npc_tab.calc_bias())
    print("Created NPC = ", [n])

    # save to the pickle
    # with open('npc_metrics.pkl', 'wb') as f:
    # pickle.dump([mme], f)

# Now loop through thresholds...

