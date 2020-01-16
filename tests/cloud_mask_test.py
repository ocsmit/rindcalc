import os
import numpy as np
from osgeo import gdal
from glob import glob
from rindcalc import cloud_mask

landsat_dir = 'C:/Landsat_8/aoi'
ndvi_out = 'C:/tmp/NDVI_C.tif'


def NDVI(landsat_dir, ndvi_out, mask_clouds):
    """
    :param landsat_dir:
    :param ndvi_out:
    :return:
    """
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
    
    if mask_clouds == True:
        cloud_mask(nir_band)
        cloud_mask(red_band)

    # Perform Calculation
    ndvi = ((nir_band - red_band) / (nir_band + red_band))

    # Save Raster
    if os.path.exists(ndvi_out):
        raise IOError('NDVI raster already created')
    if not os.path.exists(ndvi_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = ndvi.shape
        dst_ds = driver.Create(ndvi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(ndvi)
        dst_ds.FlushCache()
        dst_ds = None

    return ndvi, print('NDVI raster created.')
