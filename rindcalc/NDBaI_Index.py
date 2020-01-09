import os
import numpy as np
from osgeo import gdal
from glob import glob


def NDBaI_Index(landsat_dir, ndbai_out):
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

    # Perform Calculation
    ndbai = ((swir1_band - tir_band) / (swir1_band + tir_band))

    # Save Raster
    if os.path.exists(ndbai_out):
        raise IOError('NDBaI raster already created')
    if not os.path.exists(ndbai_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = ndbai.shape
        dst_ds = driver.Create(ndbai_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(ndbai)
        dst_ds.FlushCache()
        dst_ds = None

    return ndbai, print('NDBaI index created')
