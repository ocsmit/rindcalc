# ------------------------------------------------------------------------------
# Name: rindcalc.ls.indices.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import os
import numpy as np
from osgeo import gdal
from glob import glob
from .cloud_masking import cloud_mask_array
from rindcalc.band_utils import save_raster


def AWEIsh(landsat_dir, aweish_out=None, mask_clouds=False):
    """
    AWEIsh(landsat_dir, aweish_out, mask_clouds=False)

    Calculates the Automated Water Extraction Index (shadow) with Landsat-8
    and outputs a TIFF raster file.

    AWEIsh = (Blue + 2.5 * Green - 1.5 * (NIR + SWIR1) - 0.25 *
                SWIR2) /  (Blue + Green + NIR + SWIR1 + SWIR2)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            aweish_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    blue = glob(os.path.join(landsat_dir, '*B2*'))
    green = glob(os.path.join(landsat_dir, '*B3*'))
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    swir1 = glob(os.path.join(landsat_dir, '*B6*'))
    swir2 = glob(os.path.join(landsat_dir, '*B7*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    blue_path = gdal.Open(os.path.join(landsat_dir, blue[0]))
    blue_band = blue_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = green_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR2_path = gdal.Open(os.path.join(landsat_dir, swir2[0]))
    swir2_band = SWIR2_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, blue[0]))

    equation = ((blue_band + 2.5 * green_band - 1.5 * (nir_band + swir1_band)
                 - 0.25 * swir2_band) / (blue_band + green_band + nir_band +
                                         swir1_band + swir2_band))

    if aweish_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, aweish_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, aweish_out, snap)
            return equation
    if aweish_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def AWEInsh(landsat_dir, aweinsh_out=None, mask_clouds=False):
    """
    AWEInsh(landsat_dir, aweinsh_out, mask_clouds=False)

    Calculates the Automated Water Extraction Index (no shadow) with Landsat-8
    and outputs a TIFF raster file.

    AWEInsh = (4 * (Green - SWIR1) - (0.25 * NIR + 2.75 *
                SWIR1)) /  (Green + SWIR1 + NIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            aweinsh_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    blue = glob(os.path.join(landsat_dir, '*B2*'))
    green = glob(os.path.join(landsat_dir, '*B3*'))
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    swir1 = glob(os.path.join(landsat_dir, '*B6*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = green_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)

    snap = gdal.Open(os.path.join(landsat_dir, blue[0]))

    equation = ((4 * (green_band - swir1_band) -
                 (0.25 * nir_band + 2.75 * swir1_band)) /
                (green_band + swir1_band + nir_band))

    if aweinsh_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, aweinsh_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, aweinsh_out, snap)
            return equation
    if aweinsh_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def NDMI(landsat_dir, ndmi_out=None, mask_clouds=False):
    """
    NDMI(landsat_dir, ndmi_out)

    Calculates the Normalized Difference Moisture Index with Landsat-8
    and outputs a TIFF raster file.

    NDMI = (NIR - SWIR1) / (NIR + SWIR1)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ndmi_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    swir1 = glob(os.path.join(landsat_dir, '*B6*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, nir[0]))

    # calculation
    equation = ((nir_band - swir1_band) / (nir_band + swir1_band))

    if ndmi_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, ndmi_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, ndmi_out, snap)
            return equation
    if ndmi_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def MNDWI(landsat_dir, mndwi_out=None, mask_clouds=False):
    """
    MNDWI(landsat_dir, mndwi_out)

    Calculates the Modified Normalized Difference Water Index with Landsat-8
    and outputs a TIFF raster file.

    MNDWI = (Green - SWIR1) / (Green + SWIR1)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            mndwi_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    green = glob(os.path.join(landsat_dir, '*B3*'))
    swir1 = glob(os.path.join(landsat_dir, '*B6*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = green_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, green[0]))

    # calculation
    equation = ((green_band - swir1_band) / (green_band + swir1_band))

    if mndwi_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, mndwi_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, mndwi_out, snap)
            return equation
    if mndwi_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def NDVI(landsat_dir, ndvi_out=None, mask_clouds=False):
    """
    NDVI(landsat_dir, ndvi_out, mask_clouds=False)

    Calculates the Normalized Difference Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    NDVI = ((NIR - Red) / (NIR + Red))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ndvi_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    red = glob(os.path.join(landsat_dir, '*B4*'))
    nir = glob(os.path.join(landsat_dir, '*B5*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = red_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, red[0]))

    equation = ((nir_band - red_band) / (nir_band + red_band))

    if ndvi_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, ndvi_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, ndvi_out, snap)
            return equation
    if ndvi_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def GNDVI(landsat_dir, gndvi_out=None, mask_clouds=False):
    """
    GNDVI(landsat_dir, gndvi_out)

    Calculates the Green Normalized Difference Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    GNDVI = (NIR - Green) / (NIR + Green)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            gndvi_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    green = glob(os.path.join(landsat_dir, '*B3*'))
    nir = glob(os.path.join(landsat_dir, '*B5*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = green_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, green[0]))

    # Perform Calculation
    equation = ((nir_band - green_band) / (nir_band + green_band))

    if gndvi_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, gndvi_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, gndvi_out, snap)
            return equation
    if gndvi_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def SAVI(landsat_dir, savi_out=None, soil_brightness=0.5, mask_clouds=False):
    """
    SAVI(landsat_dir, soil_brightness=0.5, savi_out)

    Calculates the Soil Adjusted Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
                                        *L = Soil BrightnessFactor*

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            savi_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            soil_brightness :: float, required (default=0.5)

             mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    red = glob(os.path.join(landsat_dir, '*B4*'))
    nir = glob(os.path.join(landsat_dir, '*B5*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = red_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, red[0]))

    # Perform Calculation
    equation = ((nir_band - red_band) /
                (nir_band + red_band + soil_brightness)) * (1 + soil_brightness)

    if savi_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, savi_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, savi_out, snap)
            return equation
    if savi_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def ARVI(landsat_dir, arvi_out=None, mask_clouds=False):
    """
    ARVI(landsat_dir, arvi_out)

    Calculates the Atmospherically Resistant Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    ARVI = (NIR - (2 * Red) + Blue) / (NIR + (2 * Red) + Blue)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            arvi_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    red = glob(os.path.join(landsat_dir, '*B4*'))
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    blue = glob(os.path.join(landsat_dir, '*B2*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = red_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    blue_path = gdal.Open(os.path.join(landsat_dir, blue[0]))
    blue_band = blue_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, red[0]))

    # Perform Calculation
    equation = ((nir_band - (2 * red_band) + blue_band) /
                (nir_band + (2 * red_band) + blue_band))

    if arvi_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, arvi_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, arvi_out, snap)
            return equation
    if arvi_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def VARI(landsat_dir, vari_out=None, mask_clouds=False):
    """
    VARI(landsat_dir, vari_out)

    Calculates the Visual Atmospherically Resistant Index with Landsat-8
    and outputs a TIFF raster file.

    VARI = ((Green - Red) / (Green + Red - Blue))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            vari_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    blue = glob(os.path.join(landsat_dir, '*B2*'))
    green = glob(os.path.join(landsat_dir, '*B3*'))
    red = glob(os.path.join(landsat_dir, '*B4*'))

    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    blue_path = gdal.Open(os.path.join(landsat_dir, blue[0]))
    blue_band = blue_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = green_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = red_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, red[0]))

    equation = ((green_band - red_band) / (green_band + red_band - blue_band))

    if vari_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, vari_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, vari_out, snap)
            return equation
    if vari_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def NDBI(landsat_dir, ndbi_out=None, mask_clouds=False):
    """
    NDBI(landsat_dir, ndbi_out)

    Calculates the Normalized Difference Built-up Index with Landsat-8
    and outputs a TIFF raster file.

    NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ndbi_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    swir1 = glob(os.path.join(landsat_dir, '*B6*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, nir[0]))

    # Perform Calculation
    equation = ((swir1_band - nir_band) / (swir1_band + nir_band))

    # Save Raster
    if ndbi_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, ndbi_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, ndbi_out, snap)
            return equation
    if ndbi_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def NDBaI(landsat_dir, ndbai_out=None, mask_clouds=False):
    """
    NDBaI(landsat_dir, ndbai_out)

    Calculates the Normalized Difference Bareness Index with Landsat-8
    and outputs a TIFF raster file.

    NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ndbai_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    swir1 = glob(os.path.join(landsat_dir, '*B6*'))
    tir = glob(os.path.join(landsat_dir, '*B10*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    TIR_path = gdal.Open(os.path.join(landsat_dir, tir[0]))
    tir_band = TIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, tir[0]))

    # Perform Calculation
    equation = ((swir1_band - tir_band) / (swir1_band + tir_band))

    if ndbai_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, ndbai_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, ndbai_out, snap)
            return equation
    if ndbai_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def NBLI(landsat_dir, nbli_out=None, mask_clouds=False):
    """
    NBLI(landsat_dir, nbli_out)

    Calculates the Normalized Difference Bareland Index with Landsat-8
    and outputs a TIFF raster file.

    NBLI = (Red - TIR) / (Red + TIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            nbli_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    red = glob(os.path.join(landsat_dir, '*B4*'))
    tir = glob(os.path.join(landsat_dir, '*B10*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = red_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    TIR_path = gdal.Open(os.path.join(landsat_dir, tir[0]))
    tir_band = TIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, red[0]))

    # Perform Calculation
    equation = ((red_band - tir_band) / (red_band + tir_band))

    if nbli_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, nbli_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, nbli_out, snap)
            return equation
    if nbli_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def EBBI(landsat_dir, ebbi_out=None, mask_clouds=False):
    """
    EBBI(landsat_dir, ebbi_out)

    Calculates the Enhanced Built-up and Bareness Index with Landsat-8
    and outputs a TIFF raster file.

    EBBI = (SWIR1 - NIR) / (10 * (sqrt(SWIR1 + tir)))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ebbi_out :: str, optional (default=None)
                * Output path and file name for calculated index raster

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    swir1 = glob(os.path.join(landsat_dir, '*B6*'))
    tir = glob(os.path.join(landsat_dir, '*B10*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    TIR_path = gdal.Open(os.path.join(landsat_dir, tir[0]))
    tir_band = TIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, nir[0]))

    # calculation
    ebbi = ((swir1_band - nir_band) / (10 * ((swir1_band + tir_band) ** 0.5)))
    ebbi[np.isneginf(ebbi)] = 0
    ebbi_mask = np.ma.MaskedArray(ebbi, mask=(ebbi == 0))
    ebbi_mask.reshape(ebbi.shape)

    if ebbi_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, ebbi_mask)
            save_raster(masked, ebbi_out, snap)
            return masked
        if not mask_clouds:
            save_raster(ebbi_mask, ebbi_out, snap)
            return ebbi_mask
    if ebbi_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, ebbi_mask)
            return masked
        if not mask_clouds:
            return ebbi_mask


def UI(landsat_dir, ui_out=None, mask_clouds=False):
    """
    UI(landsat_dir, ui_out)

    Calculates the Urban Index with Landsat-8 and outputs a TIFF raster file.

    UI = (SWIR2 - NIR) / (SWIR2 + NIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ui_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    swir2 = glob(os.path.join(landsat_dir, '*B7*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR2_path = gdal.Open(os.path.join(landsat_dir, swir2[0]))
    swir2_band = SWIR2_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, nir[0]))

    # Perform Calculation
    equation = ((swir2_band - nir_band) / (swir2_band + nir_band))

    if ui_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, ui_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, ui_out, snap)
            return equation
    if ui_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def NBRI(landsat_dir, nbri_out=None, mask_clouds=False):
    """
    NBRI(landsat_dir, nbri_out)

    Calculates the Normalized Burn Ratio Index with Landsat-8 and outputs a
    TIFF raster file.

    UI = (SWIR2 - NIR) / (SWIR2 + NIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            nbri_out :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    # Create list with file names
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    swir2 = glob(os.path.join(landsat_dir, '*B7*'))

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR2_path = gdal.Open(os.path.join(landsat_dir, swir2[0]))
    swir2_band = SWIR2_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, nir[0]))

    # calculation
    equation = ((nir_band - swir2_band) / (nir_band + swir2_band))

    if nbri_out is not None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            save_raster(masked, nbri_out, snap)
            return masked
        if not mask_clouds:
            save_raster(equation, nbri_out, snap)
            return equation
    if nbri_out is None:
        if mask_clouds:
            masked = cloud_mask_array(landsat_dir, equation)
            return masked
        if not mask_clouds:
            return equation


def calculate_all(landsat_dir, out_dir, mask_clouds=False):
    """
    calculate_all(landsat_dir, our_dir, mask_clouds=False):

    Calculates all indices in rindcalc.naip.indices for NAIP image and outputs
    into a specified output folder with the output file names being the name of
    the function. i.e: NDVI.tif

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

             out_dir :: str, required
                * File path of output directory.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    AWEIsh(landsat_dir, os.path.join(out_dir, 'AWEIsh.tif'), mask_clouds)
    AWEInsh(landsat_dir, os.path.join(out_dir, 'AWEInsh.tif'), mask_clouds)
    NDMI(landsat_dir, os.path.join(out_dir, 'NDMI.tif'), mask_clouds)
    MNDWI(landsat_dir, os.path.join(out_dir, 'MNDWI.tif'), mask_clouds)
    NDVI(landsat_dir, os.path.join(out_dir, 'NDVI.tif'), mask_clouds)
    GNDVI(landsat_dir, os.path.join(out_dir, 'GNDVI.tif'), mask_clouds)
    SAVI(landsat_dir, os.path.join(out_dir, 'SAVI.tif'),
         mask_clouds=mask_clouds)
    ARVI(landsat_dir, os.path.join(out_dir, 'ARVI.tif'), mask_clouds)
    NDBI(landsat_dir, os.path.join(out_dir, 'NDBI.tif'), mask_clouds)
    NDBaI(landsat_dir, os.path.join(out_dir, 'NDBaI.tif'), mask_clouds)
    NBLI(landsat_dir, os.path.join(out_dir, 'NBLI.tif'), mask_clouds)
    EBBI(landsat_dir, os.path.join(out_dir, 'EBBI.tif'), mask_clouds)
    UI(landsat_dir, os.path.join(out_dir, 'UI.tif'), mask_clouds)
    NBRI(landsat_dir, os.path.join(out_dir, 'NBRI.tif'), mask_clouds)
