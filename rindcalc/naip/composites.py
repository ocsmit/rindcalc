# ------------------------------------------------------------------------------
# Name: rindcalc.naip.composites.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import numpy as np
from osgeo import gdal
from rindcalc.band_utils import norm


def FalseColor(in_naip, out_composite):
    """
    FalseColor(landsat_dir, out_composite)

    Creates a False Color composite using NAIP imagery and outputs a TIFF
    raster file with the values normalized between 0 - 255

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

            out_composite :: str, required
                * Output path and file name for calculated index raster.
    """
    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    naip = gdal.Open(in_naip)
    red_band = norm(naip.GetRasterBand(1).ReadAsArray().astype(np.float32),
                    255, 0)
    green_band = norm(naip.GetRasterBand(2).ReadAsArray().astype(np.float32),
                      255, 0)
    nir_band = norm(naip.GetRasterBand(4).ReadAsArray().astype(np.float32),
                    255, 0)
    snap = naip

    driver = gdal.GetDriverByName('GTiff')
    metadata = driver.GetMetadata()
    shape = red_band.shape
    dst_ds = driver.Create(out_composite,
                           xsize=shape[1],
                           ysize=shape[0],
                           bands=3,
                           eType=gdal.GDT_Byte)
    proj = snap.GetProjection()
    geo = snap.GetGeoTransform()
    dst_ds.SetGeoTransform(geo)
    dst_ds.SetProjection(proj)
    dst_ds.GetRasterBand(1).WriteArray(nir_band)
    dst_ds.GetRasterBand(2).WriteArray(red_band)
    dst_ds.GetRasterBand(3).WriteArray(green_band)
    dst_ds.FlushCache()
    dst_ds = None

    print('False Color composite created.')
