import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# set style information
plt.style.use('seaborn')

# data for graphs
npc = [1, 2, 3, 4, 5]

# PoD
D1_all = 0.151, 0.051, 0.009, 0, 0
D1_hi = 0.161, 0.058, 0.013, 0.001, 0.001
D1_lo = 0.125, 0.034, 0.001, -0.001, -0.001

D5_all = 0.145, 0.026, 0.001, 0, 0.002
D5_hi = 0.176, 0.035, 0.002, 0, 0.003
D5_lo = 0.056, -0.001, -0.001, -0.001, -0.001

D9_all = 0.112, 0.015, -0.001, -0.001, -0.001
D9_hi = 0.123, 0.019, -0.002, -0.002, -0.002
D9_lo = 0.081, 0.004, 0.004, 0.004, 0.004

D13_all = 0.093, 0.015, 0.003, 0.003, 0.003
D13_hi = 0.088, 0.012, 0.002, 0.002, 0.002
D13_lo = 0.111, 0.026, 0.005, 0.005, 0.005


# -PoFD
F2_all = 0.112, 0.02, 0.004, 0.004, 0.004
F2_hi = 0.152, 0.032, 0.01, 0.008, 0.008
F2_lo =  0.095, 0.014, 0.002, 0.002, 0.002

F6_all = 0.066, 0.004, 0.002, 0.002, 0.002
F6_hi = 0.117, 0.007, 0.003, 0.003, 0.003
F6_lo = 0.035, 0.002, 0.001, 0.001, 0.001

F10_all = 0.045, 0.004, 0.001, 0.001, 0
F10_hi = 0.089, 0.007, 0.003, 0.003, 0.003
F10_lo = 0.012, 0.002, 0, 0, 0

F14_all = 0.042, 0.004, 0, 0, 0
F14_hi = 0.083, 0.007, 0.001, 0.001, 0.001
F14_lo = 0.111, 0.001, 0, 0, 0

# HSS
H3_all = 0.032, 0.03, 0.005, -0.003, -0.003
H3_hi = 0.074, 0.044, 0.008, -0.003, -0.003
H3_lo =  -0.04, 0.005, -0.002, -0.004, -0.004

H7_all = 0.026, 0.005, -0.002, -0.003, -0.003
H7_hi = 0.044, 0.008, -0.001, -0.003, -0.003
H7_lo =  -0.052, -0.005, -0.003, -0.003, -0.003

H11_all = 0.013, 0.005, -0.003, -0.003, -0.003
H11_hi = -0.004, 0.008, -0.006, -0.006, -0.006
H11_lo = 0.018, -0.005, 0.003, 0.003, 0.003

H15_all = -0.006, 0.005, 0.001, 0.001, 0.001
H15_hi = -0.044, -0.001, 0.001, 0.001, 0.001
H15_lo = 0.047, 0.017, 0.003, 0.003, 0.003

# Bias
B4_all = 1.092, 0.891, 0.833, 0.823, 0.823
B4_hi = 1.001, 0.843, 0.788, 0.775, 0.775
B4_lo = 1.306, 1.005, 0.939, 0.937, 0.937

B8_all = 1.073, 0.806, 0.774, 0.772, 0.772
B8_hi = 1.027, 0.751, 0.711, 0.71, 0.71
B8_lo = 1.206, 0.962, 0.952, 0.952, 0.952

B12_all = 1.037, 0.783, 0.755, 0.755, 0.755
B12_hi = 1.017, 0.733, 0.703, 0.703, 0.703
B12_lo = 1.206, 0.93, 0.909, 0.909, 0.909

B16_all = 1.068, 0.771, 0.739, 0.739, 0.739
B16_hi = 1.009, 0.687, 0.655, 0.655, 0.655
B16_lo = 1.266, 1.053, 1.021, 1.021, 1.021


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
ax4.legend(loc='upper right', edgecolor='white', framealpha=1,
           title='Magnetometers')
plt.show()