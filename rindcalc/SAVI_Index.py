import os
import numpy as np
from osgeo import gdal
from glob import glob


def SAVI_Index(landsat_dir, soil_brightness, savi_out):
    # Create list with file names
    red = glob(landsat_dir + "/*B4.tif")
    nir = glob(landsat_dir + "/*B5.tif")

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = red_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, red[0]))

    # Perform Calculation
    savi = ((nir_band - red_band) / (nir_band + red_band + soil_brightness)) * (1 + soil_brightness)

    # Save Raster
    if os.path.exists(savi_out):
        raise IOError('SAVI raster already created')
    if not os.path.exists(savi_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = savi.shape
        dst_ds = driver.Create(savi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(savi)
        dst_ds.FlushCache()
        dst_ds = None

    return print('SAVI index created.')