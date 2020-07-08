# ------------------------------------------------------------------------------
# Name: rindcalc.ls.indices.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import os
import numpy as np
from osgeo import gdal
from rindcalc.utils import load_ls
from rindcalc.utils import save_ls


def AWEIsh(landsat_dir, out_tif=None, mask_clouds=False):
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

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """

    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    a = (bands["blue"] + 2.5 * bands["green"] - 1.5 *
         (bands["nir"] + bands["swir1"]) - 0.25 * bands["swir2"])
    b = (bands["blue"] + bands["blue"] + bands["nir"] + bands["swir1"]
         + bands["swir2"])
    equation = (a / b)

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def AWEInsh(landsat_dir, out_tif=None, mask_clouds=False):
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

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    
    bands = load_ls(landsat_dir)

    equation = ((4 * (bands["green"] - bands["swir1"]) -
                 (0.25 * bands["nir"] + 2.75 * bands["swir1"])) /
                (bands["green"] + bands["swir1"] + bands["nir"]))

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def NDMI(landsat_dir, out_tif=None, mask_clouds=False):
    """
    NDMI(landsat_dir, ndmi_out)

    Calculates the Normalized Difference Moisture Index with Landsat-8
    and outputs a TIFF raster file.

    NDMI = (NIR - SWIR1) / (NIR + SWIR1)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """

    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    # calculation
    equation = ((bands["nir"] - bands["swir1"]) / 
                (bands["nir"] + bands["swir1"]))

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def MNDWI(landsat_dir, out_tif=None, mask_clouds=False):
    """
    MNDWI(landsat_dir, mndwi_out)

    Calculates the Modified Normalized Difference Water Index with Landsat-8
    and outputs a TIFF raster file.

    MNDWI = (Green - SWIR1) / (Green + SWIR1)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    # calculation
    equation = ((bands["green"] - bands["swir1"]) / 
                (bands["green"] + bands["swir1"]))

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def NDVI(landsat_dir, out_tif=None, mask_clouds=False):
    """
    NDVI(landsat_dir, ndvi_out, mask_clouds=False)

    Calculates the Normalized Difference Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    NDVI = ((NIR - Red) / (NIR + Red))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    equation = ((bands["nir"] - bands["red"]) / 
                (bands["nir"] + bands["red"]))

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def GNDVI(landsat_dir, out_tif=None, mask_clouds=False):
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

    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    # Perform Calculation
    equation = ((bands["nir"] - bands["green"])
                / (bands["nir"] + bands["green"]))

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def SAVI(landsat_dir, out_tif=None, soil_brightness=0.5, mask_clouds=False):
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

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            soil_brightness :: float, required (default=0.5)

             mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """

    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    # Perform Calculation
    equation = ((bands["nir"] - bands["red"]) /
                (bands["nir"] + bands["red"] + soil_brightness)) \
               * (1 + soil_brightness)

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def ARVI(landsat_dir, out_tif=None, mask_clouds=False):
    """
    ARVI(landsat_dir, arvi_out)

    Calculates the Atmospherically Resistant Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    ARVI = (NIR - (2 * Red) + Blue) / (NIR + (2 * Red) + Blue)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """

    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    # Perform Calculation
    equation = ((bands["nir"] - (2 * bands["red"]) + bands["blue"]) /
                (bands["nir"] + (2 * bands["red"]) + bands["blue"]))
    
    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def VARI(landsat_dir, out_tif=None, mask_clouds=False):
    """
    VARI(landsat_dir, vari_out)

    Calculates the Visual Atmospherically Resistant Index with Landsat-8
    and outputs a TIFF raster file.

    VARI = ((Green - Red) / (Green + Red - Blue))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    equation = ((bands["green"] - bands["red"]) / 
                (bands["green"] + bands["red"] - bands["blue"]))

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def NDBI(landsat_dir, out_tif=None, mask_clouds=False):
    """
    NDBI(landsat_dir, ndbi_out)

    Calculates the Normalized Difference Built-up Index with Landsat-8
    and outputs a TIFF raster file.

    NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    # Perform Calculation
    equation = ((bands["swir1"] - bands["nir"]) / (bands["swir1"] + bands["nir"]))

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def NDBaI(landsat_dir, out_tif=None, mask_clouds=False):
    """
    NDBaI(landsat_dir, ndbai_out)

    Calculates the Normalized Difference Bareness Index with Landsat-8
    and outputs a TIFF raster file.

    NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """
    
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    # Perform Calculation
    equation = ((bands["swir1"] - bands["tir"]) / 
                (bands["swir1"] + bands["tir"]))

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def NBLI(landsat_dir, out_tif=None, mask_clouds=False):
    """
    NBLI(landsat_dir, nbli_out)

    Calculates the Normalized Difference Bareland Index with Landsat-8
    and outputs a TIFF raster file.

    NBLI = (Red - TIR) / (Red + TIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """

    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)
    
    # Perform Calculation
    equation = ((bands["red"] - bands["tir"]) / 
                (bands["red"] + bands["tir"]))

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def EBBI(landsat_dir, out_tif=None, mask_clouds=False):
    """
    EBBI(landsat_dir, ebbi_out)

    Calculates the Enhanced Built-up and Bareness Index with Landsat-8
    and outputs a TIFF raster file.

    EBBI = (SWIR1 - NIR) / (10 * (sqrt(SWIR1 + tir)))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """

    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    # calculation
    ebbi = ((bands["swir1"] - bands["nir"]) / 
            (10 * ((bands["swir1"] + bands["tir"]) ** 0.5)))
    ebbi[np.isneginf(ebbi)] = 0
    ebbi_mask = np.ma.MaskedArray(ebbi, mask=(ebbi == 0))
    ebbi_mask.reshape(ebbi.shape)

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, ebbi_mask, bands)

    return out_ras


def UI(landsat_dir, out_tif=None, mask_clouds=False):
    """
    UI(landsat_dir, ui_out)

    Calculates the Urban Index with Landsat-8 and outputs a TIFF raster file.

    UI = (SWIR2 - NIR) / (SWIR2 + NIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """

    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    # Perform Calculation
    equation = ((bands["swir2"] - bands["nir"]) /
                (bands["swir2"] + bands["nir"]))

    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


def NBRI(landsat_dir, out_tif=None, mask_clouds=False):
    """
    NBRI(landsat_dir, nbri_out)

    Calculates the Normalized Burn Ratio Index with Landsat-8 and outputs a
    TIFF raster file.

    UI = (SWIR2 - NIR) / (SWIR2 + NIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            out_tif :: str, optional (default=None)
                * Output path and file name for calculated index raster.

            mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
    """

    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    bands = load_ls(landsat_dir)

    # calculation
    equation = ((bands["nir"] - bands["swir2"]) /
                (bands["nir"] + bands["swir2"]))


    out_ras = save_ls(out_tif, mask_clouds, landsat_dir, equation, bands)

    return out_ras


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
