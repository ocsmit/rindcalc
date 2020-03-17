# ------------------------------------------------------------------------------
# Name: rindcalc.band_utils.py
# Author: Owen Smith, University of North Georgia IESA
# Purpose: Misc. band functions for rindcalc
# ------------------------------------------------------------------------------

import os
from glob import glob
from osgeo import gdal
import numpy as np


def norm(array, max_value, min_value):
    array_min, array_max = array.min(), array.max()
    return ((max_value - 0) * ((array - array_min) /
            (array_max - array_min))) + min_value


def save_raster(in_array, out, snap, dType=gdal.GDT_Float32):
    """
    save_raster(in_array, out, snap, dType=gdal.GDT_Float32)

    Saves the input NumPy array as a one band raster.

    Parameters:

            in_array :: array, required
                * NumPy array to be saved as TIFF raster file.

            out :: str, required
                * Output path and file name for TIFF raster file.

            snap :: gdal raster, required
                * Raster file with which projections and geotransformations
                  are based off.

            dType :: gdal datatype, required (default=gdal.GDT_Float32)_
                * Datatype to save raster as.
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
    gen_stats(raster_path)

    Prints minimum, maximum, mean, median, and standard deviation values for
    a raster.

    Parameters:

            raster_path ::str, required
                * input raster with which to generate statistical summary of.

    Returns:

            minimum, maximum, mean, median, standard deviation
    """

    path = gdal.Open(raster_path)
    input_arr = path.GetRasterBand(1).ReadAsArray().astype(np.float32)

    arr_min = np.nanmin(input_arr)
    arr_max = np.nanmax(input_arr)
    arr_mean = np.nanmean(input_arr)
    arr_med = np.nanmedian(input_arr)
    arr_std = np.nanstd(input_arr)
    print('min: ' + str(arr_min),
          'max: ' + str(arr_max),
          'mean: ' + str(arr_mean),
          'med: ' + str(arr_med),
          'std: ' + str(arr_std))
    return arr_min, arr_max, arr_mean, arr_med, arr_std
