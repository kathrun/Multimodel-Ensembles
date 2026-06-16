'''
Requires run analysis_scripts/gen_npc_mets.py
'''
# Incomplete! Either update pickels or try looping, 

import os
import pickle

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Open the pickles for all three mag sets
metfile = 'npc_metrics_mags_all.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/npc_metrics_mags_all.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled all mags data.'
                            'See docstring.')

with open('npc_metrics_mags_all.pkl', 'rb') as f:
    mme_all = pickle.load(f)

metfile = 'npc_metrics_mags_hi.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/npc_metrics_mags_hi.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled hi mags data. See docstring.')

with open('npc_metrics_mags_hi.pkl', 'rb') as f:
    mme_hi = pickle.load(f)

metfile = 'npc_metrics_mags_lo.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/npc_metrics_mags_lo.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled lo mags data. See docstring.')

with open('npc_metrics_mags_lo.pkl', 'rb') as f:
    mme_lo = pickle.load(f)

metfile = 'mean_metrics.pkl'
if not os.path.exists(metfile):
    metfile = 'analysis_scripts/mean_metrics.pkl'
if not os.path.exists(metfile):
    raise FileNotFoundError('Cannot find pickled deterministic data. '
                            'See docstring for halp')

with open('mean_metrics.pkl', 'rb') as f:
    detm, mean, medi = pickle.load(f)

# Grab data from pickle
npc = mme_all['n_members']
thresh = detm['thresh']

# Grab deterministc and calculate difference for PoD, PoFD, and HSS.
# Calculating each individual for now. Clear up with for loops

# 0.3 nT/s
pod_all = np.array(mme_all['pod03']) - detm['pod'][0]
pod_hi = np.array(mme_hi['pod03']) - detm['pod'][0]
pod_lo = np.array(mme_lo['pod03']) - detm['pod'][0]

pofd_all = (np.array(mme_all['pofd03']) - detm['pofd'][0])*(-1)
pofd_hi = (np.array(mme_hi['pofd03']) - detm['pofd'][0])*(-1)
pofd_lo = (np.array(mme_lo['pofd03']) - detm['pofd'][0])*(-1)

hss_all = np.array(mme_all['hss03']) - detm['hss'][0]
hss_hi = np.array(mme_hi['hss03']) - detm['hss'][0]
hss_lo = np.array(mme_lo['hss03']) - detm['hss'][0]

# 0.7 nT/s
pod_all = np.array(mme_all['pod07']) - detm['pod'][0]
pod_hi = np.array(mme_hi['pod07']) - detm['pod'][0]
pod_lo = np.array(mme_lo['pod07']) - detm['pod'][0]

pofd_all = (np.array(mme_all['pofd07']) - detm['pofd'][0])*(-1)
pofd_hi = (np.array(mme_hi['pofd07']) - detm['pofd'][0])*(-1)
pofd_lo = (np.array(mme_lo['pofd07']) - detm['pofd'][0])*(-1)

hss_all = np.array(mme_all['hss07']) - detm['hss'][0]
hss_hi = np.array(mme_hi['hss07']) - detm['hss'][0]
hss_lo = np.array(mme_lo['hss07']) - detm['hss'][0]

#1.1 nT/s
# Grab deterministc and calculate difference for PoD, PoFD, and HSS.
pod_all = np.array(mme_all['pod11']) - detm['pod'][0]
pod_hi = np.array(mme_hi['pod11']) - detm['pod'][0]
pod_lo = np.array(mme_lo['pod11']) - detm['pod'][0]

pofd_all = (np.array(mme_all['pofd11']) - detm['pofd'][0])*(-1)
pofd_hi = (np.array(mme_hi['pofd11']) - detm['pofd'][0])*(-1)
pofd_lo = (np.array(mme_lo['pofd11']) - detm['pofd'][0])*(-1)

hss_all = np.array(mme_all['hss11']) - detm['hss'][0]
hss_hi = np.array(mme_hi['hss11']) - detm['hss'][0]
hss_lo = np.array(mme_lo['hss11']) - detm['hss'][0]

# 1.5 nT.s 
pod_all = np.array(mme_all['pod15']) - detm['pod'][0]
pod_hi = np.array(mme_hi['pod15']) - detm['pod'][0]
pod_lo = np.array(mme_lo['pod15']) - detm['pod'][0]

pofd_all = (np.array(mme_all['pofd15']) - detm['pofd'][0])*(-1)
pofd_hi = (np.array(mme_hi['pofd15']) - detm['pofd'][0])*(-1)
pofd_lo = (np.array(mme_lo['pofd15']) - detm['pofd'][0])*(-1)

hss_all = np.array(mme_all['hss15']) - detm['hss'][0]
hss_hi = np.array(mme_hi['hss15']) - detm['hss'][0]
hss_lo = np.array(mme_lo['hss15']) - detm['hss'][0]


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