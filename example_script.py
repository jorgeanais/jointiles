from jointiles.utils import read_fits_table, write_fits_table, jointiles

"""
Example script
"""

tbl_t1 = read_fits_table('/home/jorge/Documents/DATA/cross/x_vvv-2mass-combis-gaia/t067_vvv-2mass-combi-gaia_clean.fits')
tbl_t2 = read_fits_table('/home/jorge/Documents/DATA/cross/x_vvv-2mass-combis-gaia/t105_vvv-2mass-combi-gaia_clean.fits')

tbl_out = jointiles(tbl_t1, tbl_t2)

write_fits_table(tbl_out)