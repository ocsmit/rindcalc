import os
import numpy as np
from osgeo import gdal
from glob import glob

landsat_dir = 'C:/Landsat_8/aoi'

# Create list with file names
swir1 = glob(landsat_dir + "/*B6.tif")
tir = glob(landsat_dir + "/*B10.tif")

# Open with gdal & create numpy arrays
gdal.UseExceptions()
gdal.AllRegister()
np.seterr(divide='ignore', invalid='ignore')
SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
TIR_path = gdal.Open(os.path.join(landsat_dir, tir[0]))
tir_band = TIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
snap = gdal.Open(os.path.join(landsat_dir, swir1[0]))

geo = SWIR1_path.GetGeoTransform()
geo1 = TIR_path.GetGeoTransform()
print(swir1_band)
print(geo)
print(tir_band)
print(geo1)