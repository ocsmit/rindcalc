import os
import numpy as np
from osgeo import gdal
from glob import glob


def GNDVI(landsat_dir, gndvi_out):
    # Create list with file names
    green = glob(landsat_dir + "/*B3.tif")
    nir = glob(landsat_dir + "/*B5.tif")

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = green_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, green[0]))

    # Perform Calculation
    gndvi = ((nir_band - green_band) / (nir_band + green_band))

    # Save Raster
    if os.path.exists(gndvi_out):
        raise IOError('Green NDVI raster already created')
    if not os.path.exists(gndvi_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = gndvi.shape
        dst_ds = driver.Create(gndvi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(gndvi)
        dst_ds.FlushCache()
        dst_ds = None

    return gndvi, print('Green NDVI index created.')
