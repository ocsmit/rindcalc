import os
import numpy as np
from osgeo import gdal
from glob import glob


def MSAVI2(landsat_dir, msavi2_out):
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
    msavi2 = (((2 * nir_band + 1) - (np.sqrt(((2 * nir_band + 1)**2) - 8 * (nir_band - red_band)))) / 2)
    msavi2[np.isnan(msavi2)] = 0
    msavi2_mask = np.ma.MaskedArray(msavi2, mask=(msavi2 == 0))
    msavi2_mask.reshape(msavi2.shape)
    # Save Raster
    if os.path.exists(msavi2_out):
        raise IOError('MSAVI2 raster already created')
    if not os.path.exists(msavi2_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = msavi2.shape
        dst_ds = driver.Create(msavi2_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(msavi2_mask)
        dst_ds.FlushCache()
        dst_ds = None

    return msavi2_mask, print('MSAVI2 index created.')