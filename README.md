JoinTiles
=========

> Status: In development 

This small utility is designed to full outer join two VVV-PSF tiles using their sky coordinates
and, in case of duplicated sources  (sources with close sky position within a given tolerance)
the source with lower total photometrical error is chosen.

It also includes two functions for reading and writing .fits tables according to the FITS standard.
Since astropy 4.0.1 tables are no longer masked by default and this gives me some problems with
missing values for float type columns i.e. when you write/read a file it replaces missing values
with 1e20 instead of nan. `read_fits_table` and `write_fits_table` correct this behavior.
In older versions (e.g. 3.2.1) this is not necessary.
