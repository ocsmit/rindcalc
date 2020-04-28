# ------------------------------------------------------------------------------
# Name: rindcalc.sent.indices.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import os
import numpy as np
from osgeo import gdal
from glob import glob
from rindcalc.sent.sent_utils import get_bands
from rindcalc.band_utils import save_raster


def AWEIsh(sent_dir, out_raster):

    bands = get_bands(sent_dir)

    nir = gdal.Open(bands[7])
    nir_band = nir.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red = gdal.Open(bands[3])
    red_band = red.GetRasterBand(1).ReadAsArray().astype(np.float32)
    green = gdal.Open(bands[2])
    green_band = green.GetRasterBand(1).ReadAsArray().astype(np.float32)
    blue = gdal.Open(bands[1])
    blue_band = blue.GetRasterBand(1).ReadAsArray().astype(np.float32)
    swir1 = gdal.Open(bands[11])
    swir1_band = swir1.GetRasterBand(1).ReadAsArray().astype(np.float32)
    swir2 = gdal.Open(bands[12])
    swir2_band = swir2.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = nir

    a = (blue_band + 2.5 * green_band - 1.5 * (nir_band + swir1) - 0.25 *
         swir2_band)
    b = (blue_band + green_band + nir_band + swir1_band + swir2_band)
    equation = a / b

    save_raster(equation, out_raster, snap, gdal.GDT_Float32)
    return equation, print('Finished')


def NDVI(sent_dir, out_raster):

    bands = get_bands(sent_dir)

    nir = gdal.Open(bands[7])
    nir_band = nir.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red = gdal.Open(bands[3])
    red_band = red.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(bands[7])

    equation = (nir_band - red_band) / (nir_band + red_band)

    save_raster(equation, out_raster, snap, gdal.GDT_Float32)
    return equation, print('Finished')


def SIPI(sent_dir, out_raster):

    bands = get_bands(sent_dir)

    nir = gdal.Open(bands[7])
    nir_band = nir.GetRasterBand(1).ReadAsArray().astype(np.float32)
    blue = gdal.Open(bands[1])
    blue_band = blue.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = nir

    equation = (nir_band - blue_band) / (nir_band + blue_band)

    save_raster(equation, out_raster, snap, gdal.GDT_Float32)
    return equation, print('Finished')


def ARVI(sent_dir, out_raster):

    bands = get_bands(sent_dir)

    nir = gdal.Open(bands[7])
    nir_band = nir.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red = gdal.Open(bands[3])
    red_band = red.GetRasterBand(1).ReadAsArray().astype(np.float32)
    blue = gdal.Open(bands[1])
    blue_band = blue.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = nir

    equation = ((nir_band - (2 * red_band) + blue_band) /
                (nir_band + (2 * red_band) + blue_band))

    save_raster(equation, out_raster, snap, gdal.GDT_Float32)
    return equation, print('Finished')


def ARVI(sent_dir, out_raster):

    bands = get_bands(sent_dir)

    nir = gdal.Open(bands[7])
    nir_band = nir.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red = gdal.Open(bands[3])
    red_band = red.GetRasterBand(1).ReadAsArray().astype(np.float32)
    blue = gdal.Open(bands[1])
    blue_band = blue.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = nir

    equation = ((nir_band - (2 * red_band) + blue_band) /
                (nir_band + (2 * red_band) + blue_band))

    save_raster(equation, out_raster, snap, gdal.GDT_Float32)
    return equation, print('Finished')
