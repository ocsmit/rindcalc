# ------------------------------------------------------------------------------
# Name: rindcalc.sent.indices.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import numpy as np
from osgeo import gdal
from rindcalc.utils import load_sent
from rindcalc.utils import save_index


def AWEIsh(sent_dir, out_raster):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_sent(sent_dir)

    a = (bands["band_2"] + 2.5 * bands["band_3"] - 1.5 *
         (bands["band_8"] + bands["band_11"]) - 0.25 *
         bands["band_12"])
    b = (bands["band_2"] + bands["band_3"] + bands["band_8"]
         + bands["band_11"] + bands["band_12"])
    equation = a / b

    save_index(equation, out_raster, bands["snap"], gdal.GDT_Float32)
    return equation, print('Finished')


def NDVI(sent_dir, out_raster):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_sent(sent_dir)

    equation = (bands["band_8"] - bands["band_4"]) / \
               (bands["band_8"] + bands["band_4"])

    save_index(equation, out_raster, bands["snap"], gdal.GDT_Float32)
    return equation, print('Finished')


def SIPI(sent_dir, out_raster):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_sent(sent_dir)

    equation = (bands["band_8"] - bands["band_2"]) / \
               (bands["band_8"] + bands["band_2"])

    save_index(equation, out_raster, bands["snap"], gdal.GDT_Float32)
    return equation, print('Finished')


def ARVI(sent_dir, out_raster):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_sent(sent_dir)

    equation = ((bands["band_8"] - (2 * bands["band_4"]) + bands["band_2"]) /
                (bands["band_8"] + (2 * bands["band_4"]) + bands["band_2"]))

    save_index(equation, out_raster, bands["snap"], gdal.GDT_Float32)
    return equation, print('Finished')
