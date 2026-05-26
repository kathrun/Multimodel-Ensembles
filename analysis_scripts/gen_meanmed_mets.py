#!/usr/bin/env python3

'''
This script generates all values used in Figure 2: Mean vs. Median
Forecast Comparison.

It creates PoD/PoFD/HSS/Bias for the deterministic, mean and median ensembles.
The result is saved as a Python pickle for use in future analysis.

Results are saved as "mean_metrics.pkl" and can be opened with the following:

```
import pickle
with open('mean_metrics.pkl', 'rb') as f:
    detm, mean, medi = pickle.load()
```

...where each of the three objects is a dictionary with thresholds and metrics
as key-value pairs.
'''

import pickle

import multimodtools as mmt

# Create inputs for MMT table building:
thresh = [0.3, 0.7, 1.1, 1.5]  # nT/s
tab_kwargs = {'event_set': 'all', 'mag_set': 'all'}

# Create containers for results:
detm, mean, medi = {'thresh': thresh}, {'thresh': thresh}, {'thresh': thresh}
for v in ['pod', 'pofd', 'hss', 'bias']:
    detm[v], mean[v], medi[v] = [], [], []

for t in thresh:
    print(f"Working on threshold={t}")
    # Create tables for current threshold:
    t_swmf = mmt.build_table('9_SWMF', thresh=t, **tab_kwargs)
    t_mean = mmt.build_table('Mean', thresh=t, **tab_kwargs)
    t_medi = mmt.build_table('Median', thresh=t, **tab_kwargs)

    # Calculate and store metrics.
    detm['pod'].append(t_swmf.calc_HR())
    detm['pofd'].append(t_swmf.calc_FARate())
    detm['hss'].append(t_swmf.calc_heidke())
    detm['bias'].append(t_swmf.calc_bias())
    mean['pod'].append(t_mean.calc_HR())
    mean['pofd'].append(t_mean.calc_FARate())
    mean['hss'].append(t_mean.calc_heidke())
    mean['bias'].append(t_mean.calc_bias())
    medi['pod'].append(t_medi.calc_HR())
    medi['pofd'].append(t_medi.calc_FARate())
    medi['hss'].append(t_medi.calc_heidke())
    medi['bias'].append(t_medi.calc_bias())

# Save to python pickle:
with open('mean_metrics.pkl', 'wb') as f:
    pickle.dump([detm, mean, medi], f)

