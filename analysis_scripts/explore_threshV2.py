#!/usr/bin/env python3

'''
Explore impacts of changing model's threshold (but not obs. threshold).
'''

import numpy as np
import multimodtools as mmt
import matplotlib.pyplot as plt

plt.style.use('seaborn')

# Create arrays of lowered thresholds.
thresh = .3
tScaled = np.linspace(0, .9 * thresh, 21)
threshes = thresh - tScaled

# Create an empty dictionary to store results.
results = {}

# Loop over all models.
for m in mmt.models:

    # Create a set of containers for the results of changing
    # the model thresholds.
    heidke = np.zeros(tScaled.size)
    bias = np.zeros(tScaled.size)
    pod = np.zeros(tScaled.size)
    pofd = np.zeros(tScaled.size)

    # Loop over all thresholds.
    for i, dthresh in enumerate(tScaled):
        # Create the table for the given threshold:
        table = mmt.build_table(m, thresh=thresh, modthresh=thresh-dthresh)

        # Calculate and stash the associated metrics:
        heidke[i] = table.calc_heidke()
        bias[i] = table.calc_bias()
        pod[i] = table.calc_HR()
        pofd[i] = table.calc_FARate()

    # Stash the result in the results dictionary:
    results[m] = {'heidke': heidke,
                  'bias': bias,
                  'pod': pod,
                  'pofd': pofd}

# Create a figure to plot results:
fig, axes = plt.subplots(1, 2, figsize=[20, 8])
axes = axes.flatten()

# Plot'em.
for m in mmt.models:
    axes[0].plot(threshes, results[m]['heidke'], label=mmt.models[m], linewidth = 5)
    axes[1].plot(threshes, results[m]['bias'], label=None, linewidth = 5)


# Details details.
fig.legend(loc='lower center', ncol=5, title_fontsize=18, fontsize=15)
labs = ('Heidke Skill Score', 'Bias')
for ax, lab in zip(axes, labs):
    ax.set_ylabel(lab, fontsize=20)
    ax.set_xlabel('dB/dt Threshold', fontsize = 20)
    ax.yaxis.set_tick_params(labelsize=20)
    ax.xaxis.set_tick_params(labelsize=20)
fig.suptitle('Forecast vs. Model Threshold', fontsize = 33)

plt.show()
