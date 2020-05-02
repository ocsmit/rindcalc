# ------------------------------------------------------------------------------
# Name: rindcalc.naip.indices.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import os
from osgeo import gdal
import numpy as np
from rindcalc.band_utils import save_raster, norm


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
    naip = gdal.Open(in_naip)
    red_band = naip.GetRasterBand(1).ReadAsArray().astype(np.float32)
    blue_band = naip.GetRasterBand(3).ReadAsArray().astype(np.float32)
    nir_band = naip.GetRasterBand(4).ReadAsArray().astype(np.float32)
    snap = naip

    # Perform Calculation
    equation = ((nir_band - (2 * red_band) + blue_band) /
                (nir_band + (2 * red_band) + blue_band))

    if arvi_out is not None:
        save_raster(equation, arvi_out, snap)
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
    naip = gdal.Open(in_naip)
    red_band = naip.GetRasterBand(1).ReadAsArray().astype(np.float32)
    green_band = naip.GetRasterBand(2).ReadAsArray().astype(np.float32)
    blue_band = naip.GetRasterBand(3).ReadAsArray().astype(np.float32)
    snap = naip

    # Perform Calculation
    equation = ((2 * green_band - (red_band + blue_band)) /
            (2 * green_band + (red_band + blue_band)))

    if vari_out is not None:
        save_raster(equation, vari_out, snap)
        return equation
    if vari_out is None:
        return equation


def nVARI(in_naip, nvari_out=None):
    """
    nVARI(in_naip, vari_out)

     **Normalized between -1 - 1**

    Calculates the Visual Atmospherically Resistant Index with NAIP imagery
    and outputs a TIFF raster file.

    VARI = ((Green - Red) / (Green + Red - Blue))

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

            nvari_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.
    """
    gdal.PushErrorHandler('CPLQuietErrorHandler')
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    naip = gdal.Open(in_naip)
    red_band = naip.GetRasterBand(1).ReadAsArray().astype(np.float32)
    green_band = naip.GetRasterBand(2).ReadAsArray().astype(np.float32)
    blue_band = naip.GetRasterBand(3).ReadAsArray().astype(np.float32)
    snap = naip

    # Perform Calculation
    equation = ((2 * green_band - (red_band + blue_band)) /
            (2 * green_band + (red_band + blue_band)))
    normalized_vari = norm(equation, 1, 1)

    if nvari_out is not None:
        save_raster(equation, nvari_out, snap)
        return equation
    if nvari_out is None:
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
    naip = gdal.Open(in_naip)
    red_band = naip.GetRasterBand(1).ReadAsArray().astype(np.float32)
    nir_band = naip.GetRasterBand(4).ReadAsArray().astype(np.float32)
    snap = naip

    # Perform Calculation
    equation = ((nir_band - red_band) /
                (nir_band + red_band))

    if ndvi_out is not None:
        save_raster(equation, ndvi_out, snap)
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
    naip = gdal.Open(in_naip)
    red_band = naip.GetRasterBand(1).ReadAsArray().astype(np.float32)
    nir_band = naip.GetRasterBand(4).ReadAsArray().astype(np.float32)
    snap = naip

    # Perform Calculation
    equation = (((nir_band - red_band) / (nir_band + red_band + soil_brightness))
                * (1 + soil_brightness))

    if savi_out is not None:
        save_raster(equation, savi_out, snap)
        return equation
    if savi_out is None:
        return equation


def RedRatio(in_naip, redratio_out=None):
    """
    Redequation(in_naip, soil_brightness=0.5, savi_out)

    Calculates the Soil Adjusted Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    equation = (blue_band + red_band + green_band) / red_band

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
    naip = gdal.Open(in_naip)
    red_band = naip.GetRasterBand(1).ReadAsArray().astype(np.float32)
    green_band = naip.GetRasterBand(2).ReadAsArray().astype(np.float32)
    blue_band = naip.GetRasterBand(3).ReadAsArray().astype(np.float32)
    snap = naip

    # Perform Calculation
    equation = (blue_band + red_band + green_band) / red_band

    if redratio_out is not None:
        save_raster(equation, redratio_out, snap)
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
