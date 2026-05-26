#!/usr/bin/env python
'''
Use Python's unittest module to ensure proper behavior of all
functions/scripts/etc.
'''

import numpy as np
import datetime as dt
import unittest

import multimodtools as mmt

datadir = mmt.install_dir+'data/'


# Define test case classes to group related tests together:
class TestMultiModTools(unittest.TestCase):
    '''
    Test for all functions/objects/methods in multimodeltools.py
    '''

    mod_file_db = datadir + '/deltaB/Event1/2_LFM-MIX/ABK_2_LFM-MIX_Event1.txt'
    mod_file_dt = datadir + '/dBdt/Event1/2_LFM-MIX/ABK_2_LFM-MIX_Event1.txt'

    obs_file_db = datadir + '/deltaB/Event1/Observations/abk_OBS_20031029.txt'
    obs_file_dt = datadir + '/dBdt/Event1/Observations/abk_OBS_20031029.txt'

    # Observation values for delta-B
    known_obs_db = {'time': [dt.datetime(2003, 10, 29, 0, 0, 0),
                             dt.datetime(2003, 10, 30, 23, 59, 0)],
                    'bn': np.array([-0264.3, -0042.8]),
                    'be': np.array([-0160.2, -0004.2]),
                    'bz': np.array([00043.4, 00318.9])}
    known_obs_db['bh'] = np.sqrt(known_obs_db['bn']**2+known_obs_db['be']**2)
    # Model values for delta-B
    known_mod_db = {'time': [dt.datetime(2003, 10, 29, 1, 0, 0),
                             dt.datetime(2003, 10, 30, 6, 0, 0)],
                    'bn': np.array([-84.950, -26.002]),
                    'be': np.array([14.2850, 10.243]),
                    'bz': np.array([1.49000, 13.721])}
    known_mod_db['bh'] = np.sqrt(known_mod_db['bn']**2+known_mod_db['be']**2)

    # Observation values for dBdt
    known_obs_dt = {'time': [dt.datetime(2003, 10, 29, 0, 0, 30),
                             dt.datetime(2003, 10, 30, 23, 57, 30)],
                    'dbn': np.array([-0.4267, -1.1850]),
                    'dbe': np.array([-0.1517, 0.0650]),
                    'dbz': np.array([0.1317, 0.5600])}
    known_obs_dt['dbh'] = np.sqrt(known_obs_dt['dbn']**2 +
                                  known_obs_dt['dbe']**2)
    # Model values for dBdt
    known_mod_dt = {'time': [dt.datetime(2003, 10, 29, 1, 0, 30),
                             dt.datetime(2003, 10, 30, 5, 58, 30)],
                    'dbn': np.array([0.0357, -0.0132]),
                    'dbe': np.array([-0.0055, 0.0132]),
                    'dbz': np.array([0.0200, -0.0300])}
    known_mod_dt['dbh'] = np.sqrt(known_mod_dt['dbn']**2 +
                                  known_mod_dt['dbe']**2)

    def test_read_deltaB(self):
        '''Test opening model and observation data for deltaB'''

        # Open files:
        obs = mmt.read_ccmcfile(self.obs_file_db)
        mod = mmt.read_ccmcfile(self.mod_file_db)

        # Test example model file:
        for k in self.known_mod_db.keys():
            self.assertEqual(mod[k][0], self.known_mod_db[k][0])
            self.assertEqual(mod[k][-1], self.known_mod_db[k][-1])

        # Test example observation file:
        for k in self.known_obs_db.keys():
            self.assertEqual(obs[k][0], self.known_obs_db[k][0])
            self.assertEqual(obs[k][-1], self.known_obs_db[k][-1])

    def test_read_dBdt(self):
        '''Test opening model and observation data for dBdt'''

        # Open files:
        obs = mmt.read_ccmcfile(self.obs_file_dt)
        mod = mmt.read_ccmcfile(self.mod_file_dt)

        # Test example model file:
        for k in self.known_mod_dt.keys():
            self.assertEqual(mod[k][0], self.known_mod_dt[k][0])
            self.assertEqual(mod[k][-1], self.known_mod_dt[k][-1])

        # Test example observation file:
        for k in self.known_obs_dt.keys():
            self.assertEqual(obs[k][0], self.known_obs_dt[k][0])
            self.assertEqual(obs[k][-1], self.known_obs_dt[k][-1])

    def test_read_weigel(self):
        '''
        Weigel files have a different format, check if we can still read.
        '''

        weigpath = datadir+'dBdt/Event1/3_WEIGEL/'

        mod = mmt.read_ccmcfile(weigpath + 'ABK_3_WEIGEL_Event1.txt')
        self.assertEqual(mod['time'][0], dt.datetime(2003, 10, 29, 0, 0, 30))
        self.assertEqual(mod['dbn'][8], -0.057)


# Define test case classes to group related tests together:
class TestBinTable(unittest.TestCase):
    '''
    Test creating a binary event table to match Pulkkinen 2013.
    Reference solution found at:
    https://ccmc.gsfc.nasa.gov/RoR_WWW/publications/Appendix_GeospaceValidation_PhaseI_dBdt.pdf
    '''

    # Set solutions:
    knownNanTable = {'hit': 47.0, 'miss': 58.0, 'falseP': 0.0, 'trueN': 3.0}
    knownNanMod = [0.09764942396143461, 0.07403161486824396]
    knownLfmTable = {'hit': 145, 'falseP': 1, 'miss': 151, 'trueN': 27}

    # Create a series of tables to test against:
    t_nans = mmt.build_table('2_LFM-MIX', event_set=[2], mag_set='YKC')
    t_lfm = mmt.build_table('2_LFM-MIX', event_set=[2], mag_set='hi')

    def testBinTable(self):
        '''
        Simple test of only hi-lat, LFM results:
        '''

        for x in ['hit', 'miss', 'falseP', 'trueN']:
            self.assertEqual(self.knownLfmTable[x], self.t_lfm[x])

    def testNanFix(self):
        '''Test a file with NaNs being handled properly'''

        # Binary table values:
        for x in ['hit', 'miss', 'falseP', 'trueN']:
            self.assertEqual(self.knownNanTable[x], self.t_nans[x])

        # Mod max values:
        self.assertEqual(self.knownNanMod[0], self.t_nans.modmax[0])
        self.assertEqual(self.knownNanMod[-1], self.t_nans.modmax[-1])


# Run all tests:
if __name__ == '__main__':
    unittest.main()
