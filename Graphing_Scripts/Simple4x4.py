import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# set style information
plt.style.use('seaborn')

# data for graphs
npc = [1, 2, 3, 4, 5]

# PoD
D1_all = 0.151, -0.028, -0.241, -0.418, -0.597
D1_hi = 0.162, -0.013, -0.205, -0.373, -0.578
D1_lo = 0.125, -0.064, -0.328, -0.523, -0.644

D5_all = 0.145, -0.146, -0.371, -0.502, -0.566
D5_hi = 0.176, -0.072, -0.299, -0.435, -0.578
D5_lo = 0.056, -0.36, -0.581, -0.695, -0.644

D9_all = 0.112, -0.212, -0.374, -0.45, -0.491
D9_hi = 0.123, -0.158, -0.328, -0.412, -0.462
D9_lo = 0.081, -0.373, -0.513, -0.562, -0.576

D13_all = 0.093, -0.176, -0.322, -0.356, -0.405
D13_hi = 0.088, -0.146, -0.289, -0.333, -0.39
D13_lo = 0.111, -0.272, -0.432, -0.432, -0.453


# -PoFD
F2_all = 0.112, -0.033, -0.085, -0.105, -0.109
F2_hi = 0.152, -0.028, -0.12, -0.158, -0.165
F2_lo =  0.095, -0.036, -0.071, -0.084, -0.086

F6_all = 0.066, -0.031, -0.057, -0.061, -0.064
F6_hi = 0.177, -0.049, -0.1, -0.109, -0.112
F6_lo = 0.034, -0.021, -0.031, -0.033, -0.035
 
F10_all = 0.044, -0.026, -0.05, -0.057, -0.059
F10_hi = 0.09, -0.033, -0.076, -0.089,-0.092
F10_lo = -0.013, -0.021, -0.03,- 0.033, -0.034

F14_all = 0.042, -0.026, -0.047, -0.051, -0.054
F14_hi = 0.083, -0.026, -0.063, -0.07, -0.073
F14_lo = 0.01, -0.028, -0.035, -0.038, -0.04

# HSS
H3_all = 0.032, 0.008, -0.15, -0.308, -0.489
H3_hi = 0.075, 0.008, -0.119, -0.239, -0.386
H3_lo =  -0.04, 0.002, -0.191, -0.391, -0.546

H7_all = 0.026, -0.087, -0.289, -0.443, -0.525
H7_hi = 0.044, -0.016, -0.192, -0.327, -0.406
H7_lo =  -0.052, -0.25, -0.484, -0.647, -0.697

H11_all = 0.013, -0.161, -0.314, -0.407, -0.464
H11_hi = -0.005, -0.115, -0.247, -0.334, -0.395
H11_lo =  0.018, -0.294, -0.461, -0.536, -0.557

H15_all = -0.006, -0.123, -0.269, -0.311, -0.384
H15_hi = -0.044, -0.114, -0.226, -0.276, -0.353
H15_lo =  0.047, -0.169, -0.383, -0.377, -0.411

# Bias
B4_all = 1.092, 0.754, 0.484, 0.286, 0.102 
B4_hi = 1.001, 0.745, 0.511, 0.325, 0.117
B4_lo = 1.306, 0.775, 0.42, 0.192, 0.066

B8_all = 1.073, 0.545, 0.257, 0.115, 0.045
B8_hi = 1.027, 0.571, 0.28, 0.132, 0.053
B8_lo = 1.206, 0.479, 0.191, 0.067, 0.019

B12_all = 1.037, 0.437, 0.183, 0.081, 0.032
B12_hi =  1.017, 0.469, 0.205, 0.092, 0.035
B12_lo = 1.098, 0.343, 0.119, 0.049, 0.019

B16_all = 1.068, 0.405, 0.141, 0.08, 0.017
B16_hi = 1.009, 0.421, 0.155, 0.089, 0.022
B16_lo = 1.266, 0.351, 0.096, 0.053, 0


# creating subplots
fig = plt.figure()
gs = fig.add_gridspec(4, 4)
((ax1, ax2, ax3, ax4), 
 (ax5, ax6, ax7, ax8), 
 (ax9, ax10, ax11, ax12),
 (ax13, ax14, ax15, ax16))= gs.subplots(sharex=True, sharey=False)
fig.set_tight_layout(True)
fig.set_figwidth(16)
fig.set_figheight(12)

fig.supxlabel('NPC Members Required', fontsize=16)

#0.3 Threshold plot
#plot PoD
ax1.set_title('$\Delta$PoD',fontsize=16)
ax1.set_ylabel('0.3 nT/s\nThreshold', rotation=0, labelpad=45, fontsize=16)
ax1.yaxis.set_tick_params(labelsize=12)

ax1.plot(npc, D1_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax1.plot(npc, D1_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax1.plot(npc, D1_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax1.axhline(y=0, color='grey', linestyle = "--")

#plot PoFD
ax2.set_title('-$\Delta$PoFD',fontsize=16)
ax2.yaxis.set_tick_params(labelsize=12)

ax2.plot(npc, F2_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax2.plot(npc, F2_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax2.plot(npc, F2_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax2.axhline(y=0, color='grey', linestyle="--")

#plot HSS
ax3.set_title('$\Delta$HSS',fontsize=16)
ax3.yaxis.set_tick_params(labelsize=12)

ax3.plot(npc, H3_all,'C1', marker='o', markersize='7.5', linewidth=3.75)
ax3.plot(npc,H3_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax3.plot(npc, H3_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax3.axhline(y=0, color='grey', linestyle = "--")
#ax3.fill_between(npc, y1=0, y2=0.2, color ='gainsboro')

#plot Bias
ax4.set_title('Bias',fontsize=16)
ax4.yaxis.set_tick_params(labelsize=12)

ax4.plot(npc, B4_all, 'C1', marker='o', markersize='7.5', linewidth=3.75, label="All")
ax4.plot(npc, B4_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75, label='High')
ax4.plot(npc, B4_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75, label='Low')

ax4.axhline(y=1, color='grey', linestyle = "--")



#0.7 Threshold plots
#plot PoD
ax5.plot(npc, D5_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax5.plot(npc, D5_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax5.plot(npc, D5_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax5.axhline(y=0, color='grey', linestyle = "--")
ax5.set_ylabel('0.7 nT/s\nThreshold', rotation=0, labelpad=45, fontsize=16)
ax5.yaxis.set_tick_params(labelsize=12)


#plot -PoD
ax6.plot(npc, F6_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax6.plot(npc,F6_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax6.plot(npc, F6_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax6.axhline(y=0, color='grey', linestyle = "--")
ax6.yaxis.set_tick_params(labelsize=12)

#plot HSS
ax7.plot(npc, H7_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax7.plot(npc, H7_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax7.plot(npc, H7_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax7.axhline(y=0, color='grey', linestyle = "--")
ax7.yaxis.set_tick_params(labelsize=12)

#plot Bias
ax8.plot(npc, B8_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax8.plot(npc, B8_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax8.plot(npc, B8_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax8.axhline(y=1, color='grey', linestyle = "--")
ax8.yaxis.set_tick_params(labelsize=12)

#1.1 Threshold plots
#plot PoD
ax9.plot(npc, D9_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax9.plot(npc, D9_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax9.plot(npc, D9_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax9.axhline(y=0, color='grey', linestyle = "--")
ax9.set_ylabel('1.1 nT/s\nThreshold', rotation=0, labelpad=50, fontsize=16)
ax9.yaxis.set_tick_params(labelsize=12)

#plot -PoFD
ax10.plot(npc, F10_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax10.plot(npc, F10_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax10.plot(npc, F10_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax10.axhline(y=0, color='grey', linestyle = "--")
ax10.yaxis.set_tick_params(labelsize=12)

#plot HSS
ax11.plot(npc, H11_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax11.plot(npc, H11_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax11.plot(npc, H11_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax11.axhline(y=0, color='grey', linestyle = "--")
ax11.yaxis.set_tick_params(labelsize=12)

#plot Bias
ax12.plot(npc, B12_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax12.plot(npc, B12_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax12.plot(npc, B12_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax12.axhline(y=1, color='grey', linestyle = "--")
ax12.yaxis.set_tick_params(labelsize=12)

#1.5 Threshold plots
#Plot PoD
ax13.plot(npc, D13_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax13.plot(npc, D13_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax13.plot(npc, D13_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax13.axhline(y=0, color='grey', linestyle="--")
ax13.set_ylabel('1.5 nT/s\nThreshold', rotation=0, labelpad=45, fontsize=16)
ax13.yaxis.set_tick_params(labelsize=12)
ax13.xaxis.set_tick_params(labelsize=12)

# plot -PoFD
ax14.plot(npc, F14_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax14.plot(npc, F14_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax14.plot(npc, F14_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax14.axhline(y=0, color='grey', linestyle="--")
ax14.yaxis.set_tick_params(labelsize=12)
ax14.xaxis.set_tick_params(labelsize=12)

# plot HSS
ax15.plot(npc, H15_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax15.plot(npc, H15_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax15.plot(npc, H15_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax15.axhline(y=0, color='grey', linestyle="--")
ax15.yaxis.set_tick_params(labelsize=12)
ax13.xaxis.set_tick_params(labelsize=12)

# plot Bias
ax16.plot(npc, B16_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
ax16.plot(npc, B16_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
ax16.plot(npc, B16_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

ax16.axhline(y=1, color='grey', linestyle="--")
ax16.yaxis.set_tick_params(labelsize=12)
ax16.xaxis.set_tick_params(labelsize=12)

#legend
ax4.legend(loc='center right', edgecolor='white', framealpha=1,
           title='Magnetometers')
plt.show()