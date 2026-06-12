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


def generate_mme(mag_set='all'):
    '''
    Given the mag_set and all thresholds, generate MMEs for 1 to 5 members.
    The result is saved as a python pickle named,
    mme_mags_<magset>.pkl

    ...which contains data as follows:

    mme['bias03']  # Bias for all n-member NPCs for threshold 0.3...
    '''

    npc = [1, 2, 3, 4, 5]
    threshes = [0.3, 0.7, 1.1, 1.5]
    mme = {'n_members': npc, 'thresholds': threshes}
    mets = ['pod', 'pofd', 'hss', 'bias']

    # Loop over all thresholds:
    for thresh in threshes:

        suffix = f"{int(10*thresh):02d}"

        for v in mets:
            mme[v + suffix] = []

        # Create tables for all 5 models.
        tables = {}
        for m in mmt.models:
            print(m)
            tables[mmt.models[m]] = mmt.build_table(m, event_set='all',
                                                    mag_set='all',
                                                    thresh=thresh)

        # create tables for all npc.
        npc_tab = {}

        # Setting up tables
        npc_size = tables['SWMF'].obsmax.size

        # Create time array (actual date doesn't matter in Bin. Event Analysis)
        tstart = datetime(2000, 1, 1, 0, 0, 0)
        t_npc = [tstart + timedelta(minutes=i*20 + 10)
                 for i in range(npc_size)]
        t_npc = np.array(t_npc)

        # Creating NPC tables
        for n in npc:
            mod = np.zeros(tables['SWMF'].obsmax.size)
            # Loop over each model and count how many crossed the threshold for
            # each 20 min window.
            for tab in tables:
                mod += 1*tables[tab].bool

            # Create a forecast that is either zero if <n crossed or MORE than
            # the threshold if >= n models crossed threshold.
            npc_forecast = 1.1 * thresh * (mod >= [n])
            npc_tab = BinaryEventTable(t_npc, tables['SWMF'].obsmax,
                                       t_npc, npc_forecast, thresh,
                                       window=20*60, verbose=False)

            # Append result metrics to list of metrics in our dict.
            mme['pod' + suffix].append(npc_tab.calc_HR())
            mme['pofd' + suffix].append(npc_tab.calc_FARate())
            mme['hss' + suffix].append(npc_tab.calc_heidke())
            mme['bias' + suffix].append(npc_tab.calc_bias())
            print(f"Created NPC = {n} {suffix}")

    # save to the pickle
    with open(f'npc_metrics_mags_{mag_set}.pkl', 'wb') as f:
        pickle.dump(mme, f)


if __name__ == "__main__":
    generate_mme()
    generate_mme('lo')
    generate_mme('hi')
