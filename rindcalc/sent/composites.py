# ------------------------------------------------------------------------------
# Name: rindcalc.sent.composites.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import numpy as np
from osgeo import gdal
from rindcalc.utils import norm, load_sent, save_comp


def RGB(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    bands = load_sent(sent_dir)

    norm_red = norm(bands["band_4"], 255, 0)
    norm_green = norm(bands["band_3"], 255, 0)
    norm_blue = norm(bands["band_2"], 255, 0)

    save_comp(norm_red, norm_green, norm_blue, bands["snap"])


def bathymetry(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    bands = load_sent(sent_dir)

    norm_red = norm(bands["band_4"], 255, 0)
    norm_green = norm(bands["band_3"], 255, 0)
    norm_coastal = norm(bands["band_1"], 255, 0)

    save_comp(norm_red, norm_green, norm_coastal, bands["snap"])

