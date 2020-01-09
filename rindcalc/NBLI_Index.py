import os
import numpy as np
from osgeo import gdal
from glob import glob


def NBLI_Index(landsat_dir, nbli_out):
    # Create list with file names
    red = glob(landsat_dir + "/*B4.tif")
    tir = glob(landsat_dir + "/*B10.tif")


    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = red_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    TIR_path = gdal.Open(os.path.join(landsat_dir, tir[0]))
    tir_band = TIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, red[0]))

    # Perform Calculation
    nbli = ((red_band - tir_band) / (red_band - tir_band))

    # Save Raster
    if os.path.exists(nbli_out):
        raise IOError('NBLI raster already created')
    if not os.path.exists(nbli_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = nbli.shape
        dst_ds = driver.Create(nbli_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(nbli)
        dst_ds.FlushCache()
        dst_ds = None

    return print('NBLI index created.')