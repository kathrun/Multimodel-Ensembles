#!/usr/bin/env python3

'''
This is the top-level module for the MultiModel Ensemble study.
It contains tools to read data files, create ensembles, etc.
'''

import os
import datetime as dt

import numpy as np
from dateutil.parser import parse as par

# Get install directory:
if __name__ != '__main__':
    install_dir = '/'.join(__loader__.path.split('/')[:-1])+'/'
else:
    install_dir = ''

# Get path to data directory:
datadir = install_dir+'data/'

# Critical constants for handling SWPC events/models/stations etc.
models = {'2_LFM-MIX': 'LFM-MIX',
          '3_WEIGEL': 'Weigel',
          '4_OPENGGCM': 'OpenGGCM',
          '6_WEIMER': 'Weimer2010',
          '9_SWMF': 'SWMF'}
# Sorted model names:
modnames = list(models.keys())
modnames.sort()

hilat = ['PBQ', 'SNK', 'ABK', 'YKC']  # 'HRN', 'IQA', 'MEA']
lolat = ['WNG', 'NEW', 'OTT']  # 'FUR', 'FRD', 'FRN']

# Colors for plotting:
cols = {}
colnames = ['gold', 'firebrick', 'darkorange', 'olivedrab', 'royalblue']
for m, c in zip(modnames, colnames):
    cols[m] = c

allmag = hilat+lolat

# Time limits of the events:
tlims = {1: (par('October 29th, 2003 06:00UT', ignoretz=True),
             par('October 30th, 2003 06:00UT', ignoretz=True)),
         2: (par('December 14, 2006 12:00 UT', ignoretz=True),
             par('December 16, 2006 00:00 UT', ignoretz=True)),
         3: (par('August 31, 2001 00:00 UT',   ignoretz=True),
             par('September 1, 2001 00:00 UT', ignoretz=True)),
         4: (par('August 31, 2005 10:00 UT',   ignoretz=True),
             par('September 1, 2005 12:00 UT', ignoretz=True)),
         7: (par('April 5, 2010 00:00 UT',     ignoretz=True),
             par('April 6, 2010, 00:00 UT',    ignoretz=True)),
         8: (par('August 5, 2011 09:00 UT',    ignoretz=True),
             par('August 6, 2011, 09:00 UT',   ignoretz=True))}

# Store binary event threshold values:
thres_dt = [0.3, 0.7, 1.1, 1.5]  # nT/s
thres_db = [101.6, 213.6, 317.5, 416.7]  # nT


def read_ccmcfile(filename):
    '''
    Read and parse a single SWPC file.

    Results are returned as a dictionary containing 'time', the three
    components of either deltaB (perturbation of field from quiet time
    values) or dB/dt in N-E-Z coordinates, and the "H" component (tangent
    to surface) as defined in the Pulkkinen et al study.

    '''

    # Start by opening our file:
    with open(filename, 'r') as f:
        # Parse header- we only care about figuring out if this is a
        # deltaB or dB/dt file.  This will be given in the variable name
        # line.
        trash = '    '
        while 'Year' not in trash:
            trash = f.readline()

        # Look for dBdt in variable names to determine data type:
        is_dBdt = True if 'dBdt' in trash else False

        # Skip units line:
        trash = f.readline()

        # Slurp remainder of file:
        lines = f.readlines()

    # Create output container:
    data = {}  # Empty dictionary
    nlines = len(lines)  # number of data entries

    # Time is a special data type (datetimes):
    data['time'] = np.zeros(nlines, dtype=object)

    # All others get set based on type of data in file:
    for v in ['bn', 'be', 'bz']:
        data['d'*is_dBdt + v] = np.zeros(nlines)

    # CCMC introduced lots of error in the "second" column of the time
    # entry: instead of 0 or 30, we find 30.5 or other values.  This affects
    # analysis.  So, set seconds for time entries based on file type.
    seconds = ' 30' if is_dBdt else ' 00'

    # Loop through and parse all data lines:
    for i, l in enumerate(lines):
        parts = l.split()

        # Extract date time:
        t = ' '.join(parts[:5]) + seconds
        data['time'][i] = dt.datetime.strptime(t, '%Y %m %d %H %M %S')

        # Parse remaining values:
        for v, x in zip(['bn', 'be', 'bz'], parts[-3:]):
            data['d'*is_dBdt + v][i] = x

    # Mask NaNs:
    for v in ['bn', 'be', 'bz']:
        data['d'*is_dBdt + v] = np.ma.masked_invalid(data['d'*is_dBdt + v])

    # Calculate h component:
    data['d'*is_dBdt + 'bh'] = np.sqrt(data['d'*is_dBdt + 'bn']**2 +
                                       data['d'*is_dBdt + 'be']**2)

    # Return data object to caller:
    return data


def build_table(model,  event_set='all', mag_set='all', thresh=0.3,
                window=20, debug=False, verbose=True, modthresh=None):
    '''
    Create a binary event table for *model* (must be member of *models* list)
    that includes all magnetometers included in *mag_set* (can be "all", "hi",
    or "lo") for all events listed in *event_set* and using a certain
    threshold, *thresh*.

    Parameters
    ==========
    model:str
       What model to use when building the table.  See *models* list for
       options.

    Other Parameters
    ================
    mag_set : str or list
        Set which group of magnetometers to use. Can be a list of 3-letter
        magnetometer station name codes or a string indicating what group to
        use, e.g., 'hi', 'lo', or 'all' for high latitude, mid-latitude,
        or both.

    event_set : list or 'all'
        List of event numbers to include, e.g., [1,2,8], defaults to 'all'.
        Available events are [1,2,3,4,7,8] following Pulkkinen et al., 2013.

    thresh : float, default=0.3
        Set the event threshold value; defaults to 0.3.

    modthresh : float
        Set the threshold for the model to be different then the observation.
        This is for experimental purposes only.

    window : int, default=20
        Set the interval window in minutes; defaults to 20.

    debug : Boolean, default=False
        Print extra debug info to screen.

    Examples
    ========
    Calculate table for LFM-MIX, event 1 only, high-latitude stations only:

    >>> table = mmt.build_table('2_LFM-MIX', event_set=[1], mag_set='hi')

    Calculate table for SWMF, event 1 only, low-latitude stations only,
    then print out values to screen:

    >>> table = mmt.build_table('9_SWMF', event_set=[1], mag_set='lo')
    >>> print(table)

    199 hits, 4 misses, 6 false positives, 7 true negatives.

    '''

    from validator import BinaryEventTable

    if not modthresh:
        modthresh = thresh

    # Handle mag set:
    if mag_set == 'all':
        mag_set = allmag
    elif 'hi' in mag_set:
        mag_set = hilat
    elif 'lo' in mag_set:
        mag_set = lolat
    elif type(mag_set) is str:
        mag_set = [mag_set]

    # Handle events:
    if event_set == 'all':
        event_set = [1, 2, 3, 4, 7, 8]
    elif type(event_set) == int:
        event_set = [event_set]

    # Convert window from minutes to seconds:
    window *= 60

    for ev in event_set:
        # Keep track of what magnetometers we used to build the table:
        used_mags = []

        # "Header" for debug prints:
        if debug:
            print(f"WORKING ON EVENT {ev}\n-------------------")

        for mag in mag_set:
            # Build path to model data
            f_mod = datadir + f'/dBdt/Event{ev}/{model}/{mag.upper()}' + \
                f'_{model}_Event{ev}.txt'

            # Build path to obs data
            f_obs = datadir+f'/dBdt/Event{ev}/Observations/{mag.lower()}' \
                + f'_OBS_{tlims[ev][0]:%Y%m%d}.txt'

            if debug:
                print(f'Looking for files:\n\t{f_mod}\n\t{f_obs}')

            if not os.path.exists(f_obs) or not os.path.exists(f_mod):
                if verbose:
                    print(f"Warning: magnetometer {mag} not found")
                continue

            used_mags.append(mag)

            # Open files
            mod = read_ccmcfile(f_mod)
            obs = read_ccmcfile(f_obs)

            # Compute table, add to existing hits/misses/etc.
            if 'table' not in locals():
                table = BinaryEventTable(obs['time'], obs['dbh'],
                                         mod['time'], mod['dbh'],
                                         thresh, window, trange=tlims[ev],
                                         modelcutoff=modthresh)
            else:
                table += BinaryEventTable(obs['time'], obs['dbh'],
                                          mod['time'], mod['dbh'],
                                          thresh, window, trange=tlims[ev],
                                          modelcutoff=modthresh)

        # Print off mags used in comparison
        if debug:
            print(f'Event {ev} used {len(used_mags)}:')
            for m in used_mags:
                print(f'\t{m}')

    return table
