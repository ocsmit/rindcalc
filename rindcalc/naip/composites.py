# ------------------------------------------------------------------------------
# Name: rindcalc.naip.composites.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import numpy as np
from osgeo import gdal
from rindcalc.utils import norm
from rindcalc.utils import load_naip
from rindcalc.utils import save_comp


def FalseColor(in_naip, out_composite):
    """
    FalseColor(landsat_dir, out_composite)

    Creates a False Color composite using NAIP imagery and outputs a TIFF
    raster file with the values normalized between 0 - 255

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

            out_composite :: str, required
                * Output path and file name for calculated index raster.
    """

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_naip(in_naip)

    norm_red = norm(bands["red"], 255, 0)
    norm_green = norm(bands["green"], 255, 0)
    norm_nir = norm(bands["nir"], 255, 0)

    save_comp(norm_nir, norm_red, norm_green, out_composite, bands["snap"])
