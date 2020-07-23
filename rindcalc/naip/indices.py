# ------------------------------------------------------------------------------
# Name: rindcalc.naip.indices.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import os
from osgeo import gdal
import numpy as np
from rindcalc.utils import save_index
from rindcalc.utils import norm
from rindcalc.utils import load_naip


def ARVI(in_naip, arvi_out=None):
    """
    ARVI(in_naip, arvi_out)

    Calculates the Atmospherically Resistant Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    ARVI = (NIR - (2 * Red) + Blue) / (NIR + (2 * Red) + Blue)

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

            arvi_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.
    """

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_naip(in_naip)

    # Perform Calculation
    equation = ((bands["nir"] - (2 * bands["red"]) + bands["blue"]) /
                (bands["nir"] + (2 * bands["red"]) + bands["blue"]))

    if arvi_out is not None:
        save_index(equation, arvi_out, bands["snap"])
        return equation
    if arvi_out is None:
        return equation


def VARI(in_naip, vari_out=None):
    """
     VARI(in_naip, vari_out)

    Calculates the Visual Atmospherically Resistant Index with NAIP imagery
    and outputs a TIFF raster file.

    VARI = ((Green - Red) / (Green + Red - Blue))

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

            vari_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.
    """

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_naip(in_naip)

    # Perform Calculation
    equation = ((2 * bands["green"] - (bands["red"] + bands["blue"])) /
            (2 * bands["green"] + (bands["red"] + bands["blue"])))

    if vari_out is not None:
        save_index(equation, vari_out, bands["snap"])
        return equation
    if vari_out is None:
        return equation


def NDVI(in_naip, ndvi_out=None):
    """
    NDVI(in_naip, ndvi_out, mask_clouds=False)

    Calculates the Normalized Difference Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    NDVI = ((NIR - Red) / (NIR + Red))

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

            ndvi_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.
    """

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_naip(in_naip)

    # Perform Calculation
    equation = ((bands["nir"] - bands["red"]) /
                (bands["nir"] + bands["red"]))

    if ndvi_out is not None:
        save_index(equation, ndvi_out, bands["snap"])
        return equation
    if ndvi_out is None:
        return equation


def SAVI(in_naip, savi_out=None, soil_brightness=0.5):
    """
    SAVI(in_naip, soil_brightness=0.5, savi_out)

    Calculates the Soil Adjusted Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
                                        *L = Soil BrightnessFactor*

    Parameters:

            in_naip :: str, required
                *File path for NAIP image.

            savi_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            soil_brightness :: float, required (default=0.5)
    """

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_naip(in_naip)

    # Perform Calculation
    equation = (((bands["nir"] - bands["red"]) / (bands["nir"] + bands["red"] + soil_brightness))
                * (1 + soil_brightness))

    if savi_out is not None:
        save_index(equation, savi_out, bands["snap"])
        return equation
    if savi_out is None:
        return equation


def RedRatio(in_naip, redratio_out=None):
    """
    Redequation(in_naip, soil_brightness=0.5, savi_out)

    Calculates the Soil Adjusted Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    equation = (bands["blue"] + bands["red"] + bands["green"]) / bands["red"]

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

            redratio_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.
    """

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_naip(in_naip)
    # Perform Calculation
    equation = (bands["blue"] + bands["red"] + bands["green"]) / bands["red"]

    if redratio_out is not None:
        save_index(equation, redratio_out, bands["snap"])
        return equation
    if redratio_out is None:
        return equation


def calculate_all(in_naip, out_dir):
    """
    calculate_all(in_naip, our_dir):

    Calculates all indices in rindcalc.naip.indices for NAIP image and outputs
    into a specified output folder with the output file names being the name of
    the function. i.e: NDVI.tif

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

             out_dir :: str, required
                * File path of output directory.

    """
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    NDVI(in_naip, os.path.join(out_dir, 'NDVI.tif'))
    SAVI(in_naip, os.path.join(out_dir, 'SAVI.tif'))
    ARVI(in_naip, os.path.join(out_dir, 'ARVI.tif'))
    VARI(in_naip, os.path.join(out_dir, 'VARI.tif'))
    nVARI(in_naip, os.path.join(out_dir, 'nVARI.tif'))
    RedRatio(in_naip, os.path.join(out_dir, 'Redequation.tif'))

    print('All NAIP indices saved to ', out_dir) 
