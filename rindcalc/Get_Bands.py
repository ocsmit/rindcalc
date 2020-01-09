import os
import numpy as np
from osgeo import gdal
from glob import glob


def GetBands(landsat_dir):
    # Create list with file names
    blue = glob(landsat_dir + "/*B2.tif")
    green = glob(landsat_dir + "/*B3.tif")
    red = glob(landsat_dir + "/*B4.tif")
    nir = glob(landsat_dir + "/*B5.tif")
    swir1 = glob(landsat_dir + "/*B6.tif")
    swir2 = glob(landsat_dir + "/*B7.tif")
    tir = glob(landsat_dir + "/*B10.tif")

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    blue_path = gdal.Open(os.path.join(landsat_dir, blue[0]))
    blue_band = blue_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = green_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = red_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR2_path = gdal.Open(os.path.join(landsat_dir, swir2[0]))
    swir2_band = SWIR2_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    TIR_path = gdal.Open(os.path.join(landsat_dir, tir[0]))
    tir_band = TIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)

    return blue_band, green_band, red_band, nir_band, swir1_band, swir2_band, tir_band
