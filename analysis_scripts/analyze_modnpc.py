#!/usr/bin/env python3

'''
Test script to work with dictionaries to use in modified_npc.py.
Goal to create Build_tables for all models with their modthresh.
'''
from argparse import ArgumentParser
from datetime import datetime, timedelta

import numpy as np

from validator import BinaryEventTable
import multimodtools as mmt

# From explore_thresh.py modifed scaling
PoD = {'2_LFM-MIX': 0.03, '3_WEIGEL': 0.03, '4_OPENGGCM': 0.03,
       '6_WEIMER': 0.03, '9_SWMF': 0.03}
POFD = {'2_LFM-MIX': 0.03, '3_WEIGEL': 0.03, '4_OPENGGCM': 0.03,
        '6_WEIMER': 0.03, '9_SWMF': 0.03}
HSS = {'2_LFM-MIX': 0.138, '3_WEIGEL': 0.070, '4_OPENGGCM': 0.192,
       '6_WEIMER': 0.057, '9_SWMF': 0.165}
Bias = {'2_LFM-MIX': 0.151, '3_WEIGEL': 0.840, '4_OPENGGCM': 0.205, 
        '6_WEIMER': 0.057, '9_SWMF': 0.205}

metric = Bias

# Handle command-line arguments.
# Initialize argument parser:
parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--events", type=int, nargs='+',
                    default=[1, 2, 3, 4, 7, 8],
                    help="Set the events to analyze via list of event number,"
                    + "e.g., --events 1 2 7 8")
parser.add_argument("-t", "--threshold", type=float, default=0.3,
                    help="Set the threshold for dB/dt in the binary event" +
                    "analysis. Default is 0.3, standard values are " +
                    "0.3, 0.7, 1.1, and 1.5 nT/s.")
parser.add_argument("-m", "--mags", nargs='+', type=str,
                    default=['all'],
                    help="Set which group of magnetometers to use. Can be a " +
                    "list of 3-letter magnetometer station name codes or a " +
                    "string indicating what group to use, e.g., 'hi', 'lo', " +
                    "'all' for high latitude, mid-latitude, or both. " +
                    "e.g., --mags all hi low pbq, would run 'hi' and 'low' " +
                    "magnetometers and the PBQ station by itself.")

# Process arguments:
args = parser.parse_args()

# Loop over the key mag groupings: all, hi, lo
for group in args.mags:
    # Turn our script options into function arguments:
    tab_kwargs = {'event_set': args.events, 'mag_set': group,
                  'thresh': args.threshold, 'verbose': False}

    # build tables for each model with their modthresh
    # loop through metric dictionary to build each table with their modthresh
    modtables = {}
    for m in mmt.models:
        modtables[mmt.models[m]] = mmt.build_table(m, modthresh=metric[m],
                                                   **tab_kwargs)

    # build tables without modthresh
    tables = {}
    for m in mmt.models:
        tables[mmt.models[m]] = mmt.build_table(m, **tab_kwargs)

    # Create Variables for metric comparisons
    # For deterministic, nonmodified, forecast
    det = mmt.build_table("9_SWMF", args.events, group, args.threshold)
    # For sizing
    SWMF = modtables[mmt.models['9_SWMF']]

    # Create modified NPC by counting the number of crossings in each bin
    # across all ensemble members (i.e., models)
    npc_size, obs_size = SWMF.obsmax.size, SWMF.Obs.size
    mod = np.zeros(SWMF.obsmax.size)
    for tab in modtables:
        mod += 1*modtables[tab].bool
    modified_npc_forecast = 1.1 * args.threshold * (mod >= 5)

    # Create nonmodifed NPC
    npc_size, obs_size = SWMF.obsmax.size, SWMF.Obs.size
    mod = np.zeros(SWMF.obsmax.size)
    for tab in tables:
        mod += 1*tables[tab].bool
    npc_forecast = 1.1 * args.threshold * (mod >= 5)

    # Create a synthetic time series to match the number of data points.
    # Doing this instead of relying on the original times, with multi-year
    # long gaps, greatly speeds processing.
    tstart = datetime(2000, 1, 1, 0, 0, 0)
    t_npc = [tstart + timedelta(minutes=i*20 + 10) for i in range(npc_size)]
    t_npc = np.array(t_npc)

    # Build table using times/dates and observed values from all included
    # events, stored in any of the other tables (but we'll use SWMF for ease.)
    for m in metric:
        modified_npc = BinaryEventTable(t_npc, SWMF.obsmax, t_npc,
                                        modified_npc_forecast, metric[m],
                                        window=20*60, verbose=False)  
    # Build unmodified table
    npc = BinaryEventTable(t_npc, SWMF.obsmax, t_npc, npc_forecast,
                           args.threshold, window=20*60, verbose=False)
    
    # Print metric comparison.
    print('PoD')
    print('Mod_NPC:', modified_npc.calc_HR())
    print('NPC:', npc.calc_HR())
    print('Determ:', det.calc_HR(),"\n")

    print('PoFD')
    print('Mod_NPC:', modified_npc.calc_FARate())
    print('NPC:', npc.calc_FARate())
    print('Determ:', det.calc_FARate(),"\n")

    print('HSS')
    print('Mod_NPC:', modified_npc.calc_heidke())
    print('NPC:', npc.calc_heidke())
    print('Determ:', det.calc_heidke(),"\n")

    print('Bias')
    print('Mod_NPC:', modified_npc.calc_bias())
    print('NPC:', npc.calc_bias())
    print('Determ:', det.calc_bias())