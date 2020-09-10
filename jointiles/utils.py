import numpy as np
from astropy.table import Table, hstack, vstack
from astropy.table.column import MaskedColumn, Column
from astropy.coordinates import SkyCoord
from astropy import units as u


def replace_fill_value_with_nan(table):
    """
    When an astropy table is written to fits format, mask values are replaced with 1e20 (only in the case of floats).
    This function modify this behavior replacing the 'fill value' with NaNs as FITS standard prescribes.
    This function is needed since astropy 4.0.1. In older versions (e.g. 3.2.1) this is not required.
    This only works in masked tables, since version 4 tables are not longer masked by default.
    Useful when writing a table to fits format.

    :param table:
    :return:
    """
    for col_name in table.colnames:
        if isinstance(table[col_name], MaskedColumn):
            if np.issubdtype(table[col_name].dtype, np.floating):
                table[col_name].fill_value = np.nan


def mask_nan_values(table):
    """
    Mask all nan values contained in columns of dtype=float.
    Useful when reading a fits table.

    :param table:
    :return:
    """
    for col_name in table.colnames:
        if isinstance(table[col_name], Column):
            if np.issubdtype(table[col_name].dtype, np.floating) and np.sum(np.isnan(table[col_name])) > 0:
                table[col_name] = Table.MaskedColumn(table[col_name].data,
                                                     mask=np.isnan(table[col_name].data),
                                                     unit=table[col_name].unit)


def read_fits_table(file):
    """
    Helper function to read a fits table file and translate into a astropytable
    :param file:
    :return:
    """
    table = Table.read(file, format='fits')
    mask_nan_values(table)
    return table


def write_fits_table(table, output_file):
    """
    Helper function to save an astropy table into a fits table file
    :param table:
    :param output_file:
    :return:
    """

    replace_fill_value_with_nan(table)
    table.write(output_file, format='fits', overwrite=False)


def jointiles(tbl_t1, tbl_t2, tolerance=0.34):
    """
    This function join two tiles (astropytable object) in one. Sources that are closer than
    the tolerance value (in arcseconds) are considered duplicated. Only one duplicated source
    with best total photometric error is kept.

    :param tbl_t1: tile left. An astropy table object
    :param tbl_t2: tile right. An astropy table object
    :param tolerance: angular separation in arcseconds. Sources closer than this distance are considered duplicated
    :return:
    """

    # Cross-match
    ct1 = SkyCoord(tbl_t1['ra'], tbl_t1['dec'])
    ct2 = SkyCoord(tbl_t2['ra'], tbl_t2['dec'])

    idx_t1, d2d_t1, d3d = ct1.match_to_catalog_sky(ct2)
    match_t1 = d2d_t1 <= tolerance * u.arcsec
    idx_t2, d2d_t2, d3d = ct2.match_to_catalog_sky(ct1)
    match_t2 = d2d_t2 <= tolerance * u.arcsec

    # Stack not duplicated sources
    tbl_notdupl = vstack([tbl_t1[~match_t1], tbl_t2[~match_t2]])

    # Total photometric error
    tot_err_t1 = tbl_t1['eJ'] ** 2 + tbl_t1['eH'] ** 2 + tbl_t1['eKs'] ** 2
    tot_err_t2 = tbl_t2['eJ'] ** 2 + tbl_t2['eH'] ** 2 + tbl_t2['eKs'] ** 2

    # Chose source with best total photometric error for each table
    phot_toterr_mask_t1 = tot_err_t1 <= tot_err_t2[idx_t1]
    best_from_t1 = match_t1 * phot_toterr_mask_t1

    phot_toterr_mask_t2 = tot_err_t2 < tot_err_t1[idx_t2]
    best_from_t2 = match_t2 * phot_toterr_mask_t2

    # Stack best duplicated sources
    tbl_dupl = vstack([tbl_t1[best_from_t1], tbl_t2[best_from_t2]])

    # Stack non-duplicated and duplicated sources
    tbl_out = vstack([tbl_notdupl, tbl_dupl])

    return tbl_out



