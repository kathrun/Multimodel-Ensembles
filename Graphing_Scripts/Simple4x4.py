'''
Requires run analysis_scripts/gen_npc_mets.py
'''
# Incomplete! Either update pickels or try looping, 

import os
import pickle

import numpy as np
import multimodtools as mmt
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

pofd_all = (np.array(mme_all['pofd03']) - detm['pofd'][0])
pofd_hi = (np.array(mme_hi['pofd03']) - detm['pofd'][0])
pofd_lo = (np.array(mme_lo['pofd03']) - detm['pofd'][0])

hss_all = np.array(mme_all['hss03']) - detm['hss'][0]
hss_hi = np.array(mme_hi['hss03']) - detm['hss'][0]
hss_lo = np.array(mme_lo['hss03']) - detm['hss'][0]

'''
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

# 1.1 nT/s
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
'''

# Plot all that data! 
mmt.set_plot_params()

fig = plt.figure(figsize=(10, 7), layout='constrained')
(a1, a2, a3, a4), (b1, b2, b3, b4), (c1, c2, c3, c4), (d1, d2, d3, d4)=fig.subplots(4, 4, sharex=True)

# 0.3 Thresh
a1.set_ylabel('0.3 $nT/s$\nThreshold')
a1.set_title('$\Delta$PoD')

a1.plot(npc, pod_all, '-C1', marker='o')
a1.plot(npc, pod_hi, '-C0', marker='o')
a1.plot(npc, pod_lo, '-C2', marker='o')

a2.set_title('$\Delta$PoFD')
a2.plot(npc, pofd_all, '-C1', marker='o')
a2.plot(npc, pofd_hi, '-C0', marker='o')
a2.plot(npc, pofd_lo, '-C2', marker='o')

a3.set_title('$\Delta$HSS')
a3.plot(npc, hss_all, '-C1', marker='o')
a3.plot(npc, hss_hi, '-C0', marker='o')
a3.plot(npc, hss_lo, '-C2', marker='o')

a4.set_title('Bias')
a4.plot(npc, mme_all['bias03'], '-C1', marker='o')
a4.plot(npc, mme_hi['bias03'], '-C0', marker='o')
a4.plot(npc, mme_lo['bias03'], '-C2', marker='o')

'''
#0.3 Threshold plot
#plot PoD
a1.set_title('$\Delta$PoD',fontsize=16)
a1.set_ylabel('0.3 nT/s\nThreshold', rotation=0, labelpad=45, fontsize=16)
a1.yaxis.set_tick_params(labelsize=12)

a1.plot(npc, D1_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
a1.plot(npc, D1_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
a1.plot(npc, D1_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

a1.axhline(y=0, color='grey', linestyle = "--")

#plot PoFD
a2.set_title('-$\Delta$PoFD',fontsize=16)
a2.yaxis.set_tick_params(labelsize=12)

a2.plot(npc, F2_all, 'C1', marker='o', markersize='7.5', linewidth=3.75)
a2.plot(npc, F2_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
a2.plot(npc, F2_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

a2.axhline(y=0, color='grey', linestyle="--")

#plot HSS
a3.set_title('$\Delta$HSS',fontsize=16)
a3.yaxis.set_tick_params(labelsize=12)

a3.plot(npc, H3_all,'C1', marker='o', markersize='7.5', linewidth=3.75)
a3.plot(npc,H3_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75)
a3.plot(npc, H3_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75)

a3.axhline(y=0, color='grey', linestyle = "--")

#plot Bias
a4.set_title('Bias',fontsize=16)
a4.yaxis.set_tick_params(labelsize=12)

a4.plot(npc, B4_all, 'C1', marker='o', markersize='7.5', linewidth=3.75, label="All")
a4.plot(npc, B4_hi, '-C0', marker='o', markersize='7.5', linewidth=3.75, label='High')
a4.plot(npc, B4_lo, '-C2',marker='o', markersize='7.5', linewidth=3.75, label='Low')

a4.axhline(y=1, color='grey', linestyle = "--")



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
a4.legend(loc='center right', edgecolor='white', framealpha=1,
           title='Magnetometers')
'''

plt.show()