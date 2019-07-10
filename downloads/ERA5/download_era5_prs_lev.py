"""
Filename:    download_era5_prs_level.py
Author:      Tessa Montini, tmontini@ucsb.edu
Description: Download ERA5 data on pressure levels

"""
import cdsapi

# Data directory and file names
datadir = "/home/sbarc/students/montini/data/downloads/"
fprefix = "era5.q850.6hr"

# Input parameters
var = 'specific_humidity'
level = '850'
start_yr = 1979
end_yr   = 1980

# Optional parameters
area = [15, -85, -50, -30]   # Default: global
grid = [0.5, 0.5]            # Default: 0.25 x 0.25


# Loop for downloading annual data files
for yr in range(start_yr,end_yr+1):
    outfile = datadir + "{0}.{1}.nc".format(fprefix, yr)
    c = cdsapi.Client()
    c.retrieve('reanalysis-era5-pressure-levels', 
               {'product_type'  : 'reanalysis',
                'pressure_level': level,
                'variable'      : var,
                'year'          : "{0}".format(yr),
                'month'         : ['01','02','03',
                                   '04','05','06',
                                   '07','08','09',
                                   '10','11','12'],
                'day'           : ['01','02','03',
                                   '04','05','06',
                                   '07','08','09',
                                   '10','11','12',
                                   '13','14','15',
                                   '16','17','18',
                                   '19','20','21',
                                   '22','23','24',
                                   '25','26','27',
                                   '28','29','30',
                                   '31'],
                'time'          : ['00:00','06:00',
                                   '12:00','18:00'],
                'area'          : area,
                'grid'          : grid,
                'format'        : 'netcdf'
               },
               outfile)
    print("Download complete: {filename} \n".format(filename=outfile))
