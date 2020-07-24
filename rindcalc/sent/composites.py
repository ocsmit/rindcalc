# ------------------------------------------------------------------------------
# Name: rindcalc.sent.composites.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import numpy as np
from osgeo import gdal
from rindcalc.utils import norm, load_sent, save_comp, load_comp


def natural_color(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    data = load_comp(sent_dir, ['band_4', 'band_3', 'band_2'])

    trans = gdal.Translate(out_composite, data, format='GTiff')


def false_color(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    data = load_comp(sent_dir, ['band_8', 'band_4', 'band_3'])

    trans = gdal.Translate(out_composite, data, format='GTiff')


def SWIR(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    data = load_comp(sent_dir, ['band_12', 'band_8a', 'band_4'])

    trans = gdal.Translate(out_composite, data, format='GTiff')


def bath(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    data = load_comp(sent_dir, ['band_4', 'band_3', 'band_1'])

    trans = gdal.Translate(out_composite, data, format='GTiff')


def agriculture(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    data = load_comp(sent_dir, ['band_11', 'band_8', 'band_2'])

    trans = gdal.Translate(out_composite, data, format='GTiff')


def geology(sent_dir, out_composite):

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()

    data = load_comp(sent_dir, ['band_12', 'band_11', 'band_2'])

    trans = gdal.Translate(out_composite, data, format='GTiff')

