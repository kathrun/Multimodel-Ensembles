import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# set style information
plt.style.use('seaborn')


# data for graphs
npc = [1, 2, 3, 4, 5]

# creating subplots
fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharex=True)
fig.suptitle('0.3nT/s Threshold', fontsize=33)
fig.set_figwidth(20)
fig.set_figheight(8)

#HSS
mod_b = 0.619, 0.679, 0.610, 0.427, 0.070
mod_h = 0.606, 0.718, 0.698, 0.588, 0.403
reg = 0.637, 0.613, 0.471, 0.302, 0.122

ax1.set_ylabel('HSS', fontsize=20)
ax1.set_xlabel('NPC Members Required', fontsize=20)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_tick_params(labelsize=20)
ax1.xaxis.set_tick_params(labelsize=20)

ax1.axhline(y=0.593, color='grey', linestyle="--")

ax1.plot(npc, reg, marker='o', markersize='10', color='black', linewidth=5, alpha=0.75)
ax1.plot(npc, mod_b, 'C2', marker='o', markersize='10', linewidth=5)
ax1.plot(npc, mod_h, 'C0', marker='o', markersize='10', linewidth=5)

# Bias
mod_b = 1.24, 1.021, 0.767, 0.490, 0.077
mod_h = 1.235, 1.063, 0.817, 0.702, 0.470
reg = 1.100, 0.759, 0.509, 0.301, 0.120
# set labels and titles
ax2.set_ylabel('Bias', fontsize=20)
ax2.set_xlabel('NPC Members Required', fontsize=20)
ax2.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax2.yaxis.set_tick_params(labelsize=20)
ax2.xaxis.set_tick_params(labelsize=20)



ax2.axhline(y=0.817, color='grey', linestyle="--")

ax2.plot(npc, reg, marker='o', markersize='10', color='black', linewidth=5, alpha=0.75, label='Set Threshold')
ax2.plot(npc, mod_b, 'C2', marker='o', markersize='10', linewidth=5, label='Scaled Bias')
ax2.plot(npc, mod_h, 'C0', marker='o', markersize='10', linewidth=5, label='Scaled HSS')


# legend
ax2.legend(loc='upper right', edgecolor='white', framealpha=1, fontsize=15)

plt.show()