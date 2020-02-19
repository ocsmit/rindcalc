# ------------------------------------------------------------------------------
# Name: rindcalc.bands_utils.py
# Author: Owen Smith, University of North Georgia IESA
# Purpose: Misc. band functions for rindcalc
# ------------------------------------------------------------------------------

import os
from glob import glob
from osgeo import gdal
import numpy as np


# Generic function to get landsat bands
def GetBands(landsat_dir):
    """

    :param landsat_dir:
    :return:
    """
    # Create list with file names
    blue = glob(os.path.join(landsat_dir, '*B2*'))
    green = glob(os.path.join(landsat_dir, '*B3*'))
    red = glob(os.path.join(landsat_dir, '*B4*'))
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    swir1 = glob(os.path.join(landsat_dir, '*B6*'))
    swir2 = glob(os.path.join(landsat_dir, '*B7*'))
    tir = glob(os.path.join(landsat_dir, '*B10*'))

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
    snap = red_path

    return blue_band, green_band, red_band, nir_band, swir1_band, swir2_band, \
           tir_band, snap


def save_raster(in_array, out, dType, snap):
    """

    :param dType:
    :param in_array:
    :param out:
    :param snap:
    :return:
    """
    if not os.path.exists(out):
        print('Writing raster')

    if os.path.exists(out):
        os.remove(out)
        print('Overwriting raster.')

    driver = gdal.GetDriverByName('GTiff')
    metadata = driver.GetMetadata()
    shape = in_array.shape
    dst_ds = driver.Create(out,
                           xsize=shape[1],
                           ysize=shape[0],
                           bands=1,
                           eType=dType)
    proj = snap.GetProjection()
    geo = snap.GetGeoTransform()
    dst_ds.SetGeoTransform(geo)
    dst_ds.SetProjection(proj)
    dst_ds.GetRasterBand(1).WriteArray(in_array)
    dst_ds.FlushCache()
    dst_ds = None

    return in_array


def gen_stats(raster_path):
    """

    :param raster_path:
    :return:
    """

    path = gdal.Open(raster_path)
    input_arr = path.GetRasterBand(1).ReadAsArray().astype(np.float32)

    arr_min = np.nanmin(input_arr)
    arr_max = np.nanmax(input_arr)
    arr_mean = np.nanmean(input_arr)
    arr_med = np.nanmedian(input_arr)
    arr_std = np.nanstd(input_arr)
    return print('min: ' + str(arr_min),
                 'max: ' + str(arr_max),
                 'mean: ' + str(arr_mean),
                 'med: ' + str(arr_med),
                 'std: ' + str(arr_std))
