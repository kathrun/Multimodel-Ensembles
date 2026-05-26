#!/usr/bin/env python3

'''
Small script to create forecast metric for a scaling model threshold.
'''
from argparse import ArgumentParser

import multimodtools as mmt

parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--events", type=int, nargs='+',
                    default=[1],
                    help="Set the events to analyze via list of event number,"
                    + "e.g., --events 1 2 7 8")
parser.add_argument("-m", "--mag", type=str, default='YKC',
                    help='Set the magnetometer to analyze: ABK, PBQ, ' +
                    'SNK, YKC, NEW, OTT, or WNG')
parser.add_argument("-t", "--thresh", type=float, default=0.3,
                    help="Set the threshold to analyze: 0.3, 0.7, 1.1, or 1.5")
parser.add_argument('-mt', "--modthresh", type=float, default=0.3,
                    help="Set the model's threshold to analyzie. Optimized" +
                    "Optimized bias threshold for each model is as follows:" +
                    "LFM-MIX = 0.151, Weigel = 0.084, OpenGGCM = 0.205," +
                    "Weimer = 0.057, and SWMF = 0.205.")

# Process arguments
args = parser.parse_args()

# script options into function arguments?
tab_kwargs = {'event_set': args.events, 'mag_set': args.mag,
              'thresh': args.thresh, 'modthresh': args.modthresh}

# Deterministic table
swmf = mmt.build_table('9_SWMF', **tab_kwargs)

# Tables for each model
for m in mmt.models:
    mod_tab = mmt.build_table(m, **tab_kwargs)
    print(m, f"PoD: {mod_tab.calc_HR():+6.3f}")
    print(m, f"PoFD: {mod_tab.calc_FARate():+6.3f}")
    print(m, f"Heidke: {mod_tab.calc_heidke():+6.3f}")
    print(m, f"Bias: {mod_tab.calc_bias():+6.3f}")
