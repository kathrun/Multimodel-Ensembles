# Multi-Model Ensemble Analysis

This repository contains tools and data to perform a proof-of-concept study
on multi-model ground magnetic perturbation forecasting.

## Data
All data was obtained from the [CCMC website that shares the
Pulkkinen et al., 2013 results](https://ccmc.gsfc.nasa.gov/challenges/dBdt/timeseries.php).

The file format for many of these files are inconsistent or incorrect; the
`fix_headers.py` script can and *has* been used to fix issues with file
headers.

## Generating Data

Ensemble data must be generated manually before performing analysis.
Data is saved as Python pickles.

Type this to get ...
```
python command here from import to final command
```
## Dependencies

This table quickly summarizes what is needed:
| Library/Software Name | Description |
| --------------------------|------------------------|
|Python 3.X  | Most scripts use Python 3.x |
|Numpy  >=1.16.X | Requirement for Spacepy |
|Matplotlib =3.1.X | All visualization done with MPL. |
|Scipy 1.3.X | Requirement for Spacepy |
|Spacepy >=0.2.3| Handles SWMF output, expedites visualization. |
|[Validator](https://github.com/spacecataz/validator) | Performs binary event validation. |

