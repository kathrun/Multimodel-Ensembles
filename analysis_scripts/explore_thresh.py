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
fig, axes = plt.subplots(2, 2, figsize=[8, 8])
axes = axes.flatten()

# Plot'em.
for m in mmt.models:
    axes[0].plot(threshes, results[m]['heidke'], label=mmt.models[m])
    axes[1].plot(threshes, results[m]['bias'], label=None)
    axes[2].plot(threshes, results[m]['pod'], label=None)
    axes[3].plot(threshes, results[m]['pofd'], label=None)

# Details details.
fig.legend(loc='lower center', ncol=3)
labs = ('Heidke Skill Score', 'Bias', 'Prob. of Detection', 'False Alarm Rate')
for ax, lab in zip(axes, labs):
    ax.set_ylabel(lab)
    ax.set_xlabel('dB/dt Threshold')
fig.suptitle('Forecast vs. Model Threshold')

# These values create a nice, tight figure with the figure legend:
fig.subplots_adjust(top=0.949, bottom=0.167, left=0.107,
                    right=0.972, hspace=0.26, wspace=0.286)


# For finding max threshold
for m in mmt.models:
    y_h = results[m]['heidke'].argmax()
    print(m, "heidke Max:", threshes[y_h])
    y_p = results[m]['pod'].argmax()
    print(m, "PoD Max:", threshes[y_p])
    y_f = results[m]['pofd'].argmax()
    print(m, "PoFD Max:", threshes[y_f], "\n")

#Calculating optimized bias
for m in mmt.models:
        b_dist =  abs(1-(results[m]['bias']))
        b_loc= b_dist.argmin()
        print(m,"Optimized Bias:", threshes[b_loc])
