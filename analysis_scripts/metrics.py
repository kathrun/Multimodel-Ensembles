#!/usr/bin/env python3

'''
Small script to create forecast metric comparison between mean and
deterministic forecasts.
'''
from argparse import ArgumentParser

import multimodtools as mmt

# Argparser lines in order to change the event, station, and model
parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--events", type=int, nargs='+',
                    default=[1],
                    help="Set the events to analyze via list of event number,"
                    + "e.g., --events 1 2 7 8")
parser.add_argument("-m", "--mags", type=str,
                    default=['all'],
                    help="Set which group of magnetometers to use. Can be a " +
                    "list of 3-letter magnetometer station name codes or a " +
                    "string indicating what group to use, e.g., 'hi', 'lo', " +
                    "'all' for high latitude, mid-latitude, or both. " +
                    "e.g., --mags all hi low pbq, would run 'hi' and 'low' " +
                    "magnetometers and the PBQ station by itself.")
parser.add_argument("-t", "--thresh", type=float, default=0.3,
                    help="Set the threshold to analyze: 0.3, 0.7, 1.1, or 1.5")
parser.add_argument("-d", "--debug", action="store_true",
                    help="Turn on debug mode")

# Process arguments
args = parser.parse_args()

# script options into function arguments?
tab_kwargs = {'event_set': args.events, 'mag_set': args.mags, 'thresh': args.thresh}
swmf = mmt.build_table('9_SWMF', **tab_kwargs)

mod_tab = mmt.build_table('Mean', **tab_kwargs)
# mod_tab = mmt.build_table('Median', **tab_kwargs)

# calculate bias difference from 1
d = abs(1-swmf.calc_bias())
e = abs(1-mod_tab.calc_bias())
b = d-e


print(f'Station: ?\tEvent(s): {args.events}\tThreshold: {args.thresh}')
print(f'Metric | Determ | Mean | Diff \n')
print('----------------------------------\n')
print(f"  PoD  | {swmf.calc_HR():+6.3f} | {mod_tab.calc_HR():+6.3f} |" +
      f" {mod_tab.calc_HR() - swmf.calc_HR():+6.3f}\n")
print(f"  PoFD | {swmf.calc_FARate():+6.3f} | {mod_tab.calc_FARate():+6.3f} |" +
      f" {mod_tab.calc_FARate() - swmf.calc_FARate():+6.3f}\n")
print(f"  HSS  | {swmf.calc_heidke():+6.3f} | {mod_tab.calc_heidke():+6.3f} |" +
      f" {mod_tab.calc_heidke() - swmf.calc_heidke():+6.3f}\n")#
print(f"  Bias | {swmf.calc_bias():+6.3f} | {mod_tab.calc_bias():+6.3f} |" +
      f" {b:+6.3f}\n\n")