# ------------------------------------------------------------------------------
# Name: rindcalc.sent.composites.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import numpy as np
from osgeo import gdal
from rindcalc.utils import norm, load_sent, save_comp


def natural_color(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    bands = load_sent(sent_dir)

    norm_one = norm(bands["band_4"], 255, 0)
    norm_two = norm(bands["band_3"], 255, 0)
    norm_three = norm(bands["band_2"], 255, 0)

    save_comp(norm_one, norm_two, norm_three, out_composite, bands["snap"])


def false_color(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    bands = load_sent(sent_dir)

    norm_one = norm(bands["band_8"], 255, 0)
    norm_two = norm(bands["band_4"], 255, 0)
    norm_three = norm(bands["band_3"], 255, 0)

    save_comp(norm_one, norm_two, norm_three, out_composite, bands["snap"])


def SWIR(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    bands = load_sent(sent_dir)

    norm_one = norm(bands["band_12"], 255, 0)
    norm_two = norm(bands["band_8a"], 255, 0)
    norm_three = norm(bands["band_4"], 255, 0)

    save_comp(norm_one, norm_two, norm_three, out_composite, bands["snap"])


def bathymetry(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    bands = load_sent(sent_dir)

    norm_one = norm(bands["band_4"], 255, 0)
    norm_two = norm(bands["band_3"], 255, 0)
    norm_three = norm(bands["band_1"], 255, 0)

    save_comp(norm_one, norm_two, norm_three, out_composite, bands["snap"])


def agriculture(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    bands = load_sent(sent_dir)

    norm_one = norm(bands["band_11"], 255, 0)
    norm_two = norm(bands["band_8"], 255, 0)
    norm_three = norm(bands["band_2"], 255, 0)

    save_comp(norm_one, norm_two, norm_three, out_composite, bands["snap"])


def geology(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    bands = load_sent(sent_dir)

    norm_one = norm(bands["band_12"], 255, 0)
    norm_two = norm(bands["band_11"], 255, 0)
    norm_three = norm(bands["band_2"], 255, 0)

    save_comp(norm_one, norm_two, norm_three, out_composite, bands["snap"])
