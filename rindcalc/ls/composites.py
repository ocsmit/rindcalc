# ------------------------------------------------------------------------------
# Name: rindcalc.ls.composites.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import os
import numpy as np
from osgeo import gdal
from glob import glob
from rindcalc.utils import norm
from rindcalc.utils import load_ls
from rindcalc.utils import save_comp


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
    bands = load_ls(landsat_dir, np.uint16)
    norm_red = norm(bands["red"], 255, 0)
    norm_blue = norm(bands["blue"], 255, 0)
    norm_green = norm(bands["green"], 255, 0)

    save_comp(norm_red, norm_green, norm_blue, out_composite, bands["snap"])


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
    bands = load_ls(landsat_dir, np.uint16)
    norm_red = norm(bands["red"], 255, 0)
    norm_nir = norm(bands["nir"], 255, 0)
    norm_green = norm(bands["green"], 255, 0)

    save_comp(norm_nir, norm_red, norm_green, out_composite, bands["snap"])

    return print('False Color composite created.')
