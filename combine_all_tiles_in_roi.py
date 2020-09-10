from jointiles.utils import read_fits_table, write_fits_table, jointiles

t067 = read_fits_table('/home/jorge/Documents/DATA/cross/x_vvv-2mass-combis-gaia/t067_vvv-2mass-combi-gaia_clean.fits')
t0105 = read_fits_table('/home/jorge/Documents/DATA/cross/x_vvv-2mass-combis-gaia/t105_vvv-2mass-combi-gaia_clean.fits')
t067_t105 = jointiles(t067, t0105)
write_fits_table(t067_t105, '/home/jorge/t067_t105.fits')

t068 = read_fits_table('/home/jorge/Documents/DATA/cross/x_vvv-2mass-combis-gaia/t068_vvv-2mass-combi-gaia_clean.fits')
t0106 = read_fits_table('/home/jorge/Documents/DATA/cross/x_vvv-2mass-combis-gaia/t106_vvv-2mass-combi-gaia_clean.fits')
t068_t106 = jointiles(t068, t0106)
write_fits_table(t068_t106, '/home/jorge/t068_t106.fits')

t069 = read_fits_table('/home/jorge/Documents/DATA/cross/x_vvv-2mass-combis-gaia/t069_vvv-2mass-combi-gaia_clean.fits')
t0107 = read_fits_table('/home/jorge/Documents/DATA/cross/x_vvv-2mass-combis-gaia/t107_vvv-2mass-combi-gaia_clean.fits')
t069_t107 = jointiles(t069, t0107)
write_fits_table(t069_t107, '/home/jorge/t069_t107.fits')


t070 = read_fits_table('/home/jorge/Documents/DATA/cross/x_vvv-2mass-combis-gaia/t070_vvv-2mass-combi-gaia_clean.fits')
t0108 = read_fits_table('/home/jorge/Documents/DATA/cross/x_vvv-2mass-combis-gaia/t108_vvv-2mass-combi-gaia_clean.fits')
t070_t108 = jointiles(t070, t0108)
write_fits_table(t070_t108, '/home/jorge/t070_t108.fits')



t067_t105 = read_fits_table('/home/jorge/t067_t105.fits')
t068_t106 = read_fits_table('/home/jorge/t068_t106.fits')
half_1 = jointiles(t067_t105, t068_t106)
write_fits_table(half_1, '/home/jorge/half_1.fits')


t069_t107 = read_fits_table('/home/jorge/t069_t107.fits')
t070_t108 = read_fits_table('/home/jorge/t070_t108.fits')
half_2 = jointiles(t069_t107, t070_t108)
write_fits_table(half_2, '/home/jorge/half_2.fits')


half_1 = read_fits_table('/home/jorge/half_1.fits')
half_2 = read_fits_table('/home/jorge/half_2.fits')
big_tile = jointiles(half_1, half_2)
write_fits_table(big_tile, '/home/jorge/bigtile.fits')