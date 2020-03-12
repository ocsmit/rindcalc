#------------------------------------------------------------------------------
# Name: rindcalc.composite_utils.py
# Author: Owen Smith, University of North Georgia IESA
# Purpose: Functions for creating composites out of Landsat-8 bands
#------------------------------------------------------------------------------

import os
import numpy as np
from osgeo import gdal
from glob import glob


def norm(array):
    array_min, array_max = array.min(), array.max()
    return ((255 - 0) * ((array - array_min) / (array_max - array_min))) + 0


def RGB(landsat_dir, out_composite):
    """ RGB composite

    :param landsat_dir:
    :param out_composite:
    :return:
    """

    # Create list with file names
    blue = glob(os.path.join(landsat_dir, '*B2*'))
    green = glob(os.path.join(landsat_dir, '*B3*'))
    red = glob(os.path.join(landsat_dir, '*B4*'))

    blue_path = gdal.Open(os.path.join(landsat_dir, blue[0]))
    blue_band = norm(blue_path.GetRasterBand(1).ReadAsArray(
                                                          ).astype(np.uint16))
    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = norm(green_path.GetRasterBand(1).ReadAsArray(
                                                          ).astype(np.uint16))
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = norm(red_path.GetRasterBand(1).ReadAsArray().astype(np.uint16))
    snap = gdal.Open(os.path.join(landsat_dir, red[0]))

    # Save Raster
    if os.path.exists(out_composite):
        raise IOError('RGB composite raster already created')
    if not os.path.exists(out_composite):
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
        dst_ds.GetRasterBand(1).WriteArray(red_band)
        dst_ds.GetRasterBand(2).WriteArray(green_band)
        dst_ds.GetRasterBand(3).WriteArray(blue_band)
        dst_ds.FlushCache()
        dst_ds = None

    return print('RGB composite created.')


def FalseColor(landsat_dir, out_composite):
    """

    :param landsat_dir:
    :param out_composite:
    :return:
    """

    # Create list with file names
    green = glob(os.path.join(landsat_dir, '*B3*'))
    red = glob(os.path.join(landsat_dir, '*B4*'))
    nir = glob(os.path.join(landsat_dir, '*B5*'))

    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = norm(green_path.GetRasterBand(1).ReadAsArray(
                                                          ).astype(np.uint16))
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = norm(red_path.GetRasterBand(1).ReadAsArray().astype(np.uint16))
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = norm(NIR_path.GetRasterBand(1).ReadAsArray().astype(np.uint16))
    snap = gdal.Open(os.path.join(landsat_dir, red[0]))

    # Save Raster
    if os.path.exists(out_composite):
        raise IOError('False Color composite raster already created')
    if not os.path.exists(out_composite):
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

    return print('False Color composite created.')
