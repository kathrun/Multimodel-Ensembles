#set up right but need proper Bias data then copy and past for the rest

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# set style information
plt.style.use('seaborn')


# data for graphs
npc = [1, 2, 3, 4, 5]

# creating subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout='constrained', sharex=True)
fig.suptitle('0.3nT/s Threshold', fontsize=33)
fig.set_figwidth(16)
fig.set_figheight(12)

# PoD
all = 0.151, -0.028, -0.241,-0.418,-0.597
hi = 0.161, -0.013, -0.205, -0.373, -0.578
low = 0.125, -0.064, -0.328, -0.523, -0.644

# set labels and titles
ax1.set_title('$\Delta$PoD', fontsize=26)
ax1.yaxis.set_tick_params(labelsize=20)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))


# plot mag groups
ax1.plot(npc, all, 'C1', marker='o', markersize='10', linewidth=5)
ax1.plot(npc, hi, '-C0', marker='o', markersize='10', linewidth=5)
ax1.plot(npc, low, '-C2',marker='o', markersize='10', linewidth=5)

# PoFD
all = 0.112, -0.033, -0.085, -0.105, -0.109
hi = 0.152, -0.028, -0.12, -0.158, -0.165
low = 0.095, -0.036, -0.071, -0.084, -0.086

# set labels and titles
ax2.set_title('-$\Delta$PoFD', fontsize=26)
ax2.yaxis.set_tick_params(labelsize=20)


# plot mag groups
ax2.plot(npc, all, '-C1', label='All', marker='o', markersize='10', linewidth=5)
ax2.plot(npc, hi, '-C0', label='High', marker='o', markersize='10', linewidth=5)
ax2.plot(npc, low, '-C2', label="Low", marker='o', markersize='10', linewidth=5)

# HSS
all = 0.032, 0.008, -0.15, -0.308, -0.489
hi =  0.075, 0.008, -0.119, -0.239, -0.386
low =  -0.04, 0.002, -0.191, -0.391, -0.546

#set labels and titles
ax3.set_title('$\Delta$HSS', fontsize=26)
ax3.set_xlabel('NPC', fontsize=24)
ax3.xaxis.set_tick_params(labelsize=20)
ax3.yaxis.set_tick_params(labelsize=20)


# plot mag groups
ax3.plot(npc, all, '-C1', marker='o', markersize='10', linewidth=5)
ax3.plot(npc, hi, '-C0', marker='o', markersize='10', linewidth=5)
ax3.plot(npc, low, '-C2', marker='o', markersize='10', linewidth=5)

# Bias
all = 1.092, 0.754, 0.484, 0.286, 0.102
hi = 1.001, 0.745, 0.511, 0.325, 0.117
low = 1.306, 0.775, 0.42, 0.192, 0.066

# set labels and titles
ax4.set_title('Bias', fontsize=26)
ax4.set_xlabel('NPC', fontsize=24)
ax4.xaxis.set_tick_params(labelsize=20)
ax4.yaxis.set_tick_params(labelsize=20)
ax4.axhline(y=1, color='grey', linestyle="--")

# plot mag groups
ax4.plot(npc, all, '-C1', label='All', marker='o', markersize='10', linewidth=5)
ax4.plot(npc, hi, '-C0', label='High', marker='o', markersize='10', linewidth=5)
ax4.plot(npc, low, '-C2', label="Low", marker='o', markersize='10', linewidth=5)

# legend
ax4.legend(loc='upper right', edgecolor='white', framealpha=1,
           title='Magnetometers',title_fontsize=18, fontsize=15)

plt.show()