# ------------------------------------------------------------------------------
# Name: rindcalc.ls.composites.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import os
import numpy as np
from osgeo import gdal
from glob import glob
from rindcalc.band_utils import norm


def RGB(landsat_dir, out_composite):
    """
    RGB(landsat_dir, out_composite)

    Creates a RGB composite using Landsat-8 and out puts a TIFF raster file
    with the values normalized between 0 - 255

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_composite :: str, required
                * Output path and file name for calculated index raster.
    """

    # Create list with file names
    blue = glob(os.path.join(landsat_dir, '*B2*'))
    green = glob(os.path.join(landsat_dir, '*B3*'))
    red = glob(os.path.join(landsat_dir, '*B4*'))

    blue_path = gdal.Open(os.path.join(landsat_dir, blue[0]))
    blue_band = norm(blue_path.GetRasterBand(1).ReadAsArray(
    ).astype(np.uint16), 255, 0)
    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = norm(green_path.GetRasterBand(1).ReadAsArray(
    ).astype(np.uint16), 255, 0)
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = norm(red_path.GetRasterBand(1).ReadAsArray().astype(
        np.uint16), 255, 0)
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
    FalseColor(landsat_dir, out_composite)

    Creates a False Color composite using Landsat-8 and out puts a TIFF raster
    file with the values normalized between 0 - 255

    Parameters:

            landsat_dir ::str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_composite :: str, required
                * Output path and file name for calculated index raster.
    """
    # Create list with file names
    green = glob(os.path.join(landsat_dir, '*B3*'))
    red = glob(os.path.join(landsat_dir, '*B4*'))
    nir = glob(os.path.join(landsat_dir, '*B5*'))

    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = norm(green_path.GetRasterBand(1).ReadAsArray(
    ).astype(np.uint16), 255, 0)
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = norm(red_path.GetRasterBand(1).ReadAsArray().astype(
        np.uint16), 255, 0)
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = norm(NIR_path.GetRasterBand(1).ReadAsArray().astype(
        np.uint16), 255, 0)
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
