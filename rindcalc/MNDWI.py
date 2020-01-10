import os
import numpy as np
from osgeo import gdal
from glob import glob


def MNDWI(landsat_dir, mndwi_out):
    # Create list with file names
    green = glob(landsat_dir + "/*B3.tif")
    swir1 = glob(landsat_dir + "/*B6.tif")

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = green_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, green[0]))

    # calculation
    mndwi = ((green_band - swir1_band) / (green_band + swir1_band))

    # Save Raster
    if os.path.exists(mndwi_out):
        raise IOError('MNDWI raster already created')
    if not os.path.exists(mndwi_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = mndwi.shape
        dst_ds = driver.Create(mndwi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(mndwi)
        dst_ds.FlushCache()
        dst_ds = None

    return mndwi, print('MNDWI index created.')
