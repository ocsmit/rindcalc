import os
import numpy as np
from osgeo import gdal
from glob import glob


def NBRI(landsat_dir, nbri_out):
    # Create list with file names
    nir = glob(landsat_dir + "/*B5.tif")
    swir2 = glob(landsat_dir + "/*B7.tif")

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR2_path = gdal.Open(os.path.join(landsat_dir, swir2[0]))
    swir2_band = SWIR2_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, nir[0]))

    # calculation
    nbri = ((nir_band - swir2_band) / (nir_band + swir2_band))

    # Save Raster
    if os.path.exists(nbri_out):
        raise IOError('NDWI raster already created')
    if not os.path.exists(nbri_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = nbri.shape
        dst_ds = driver.Create(nbri_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(nbri)
        dst_ds.FlushCache()
        dst_ds = None

    return nbri, print('NBRI index created.')