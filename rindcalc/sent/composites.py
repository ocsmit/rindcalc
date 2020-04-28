# ------------------------------------------------------------------------------
# Name: rindcalc.sent.composites.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import os
import numpy as np
from osgeo import gdal
from glob import glob
from rindcalc.band_utils import norm
from rindcalc.sent.sent_utils import get_bands


def RGB(sent_dir, out_composite):

    bands = get_bands(sent_dir)

    red = gdal.Open(bands[3])
    red_band = norm(red.GetRasterBand(1).ReadAsArray().astype(np.float32),
                    255, 0)
    green = gdal.Open(bands[2])
    green_band = norm(green.GetRasterBand(1).ReadAsArray().astype(np.float32),
                      255, 0)
    blue = gdal.Open(bands[1])
    blue_band = norm(blue.GetRasterBand(1).ReadAsArray().astype(np.float32),
                     255, 0)
    snap = red

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


def bathymetry(sent_dir, out_composite):

    bands = get_bands(sent_dir)

    red = gdal.Open(bands[3])
    red_band = norm(red.GetRasterBand(1).ReadAsArray().astype(np.float32),
                    255, 0)
    green = gdal.Open(bands[2])
    green_band = norm(green.GetRasterBand(1).ReadAsArray().astype(np.float32),
                      255, 0)
    coastal = gdal.Open(bands[0])
    coastal_band = norm(coastal.GetRasterBand(1).ReadAsArray().astype(np.float32)
                        , 255, 0)
    snap = red

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
    dst_ds.GetRasterBand(3).WriteArray(coastal_band)
    dst_ds.FlushCache()
    dst_ds = None
