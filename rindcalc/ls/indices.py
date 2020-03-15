# ------------------------------------------------------------------------------
# Name: rindcalc.indices.py
# Author: Owen Smith, University of North Georgia IESA
# Purpose: Create a functioning python module for Landsat 8 index calculations
# ------------------------------------------------------------------------------

import os
import numpy as np
from osgeo import gdal
from glob import glob
from .cloud_masking import cloud_mask
from .bands_utils import save_raster


# Water Indices
def AWEIsh(landsat_dir, aweish_out, mask_clouds=False):
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

            aweish_out :: str, required
                * Output path and file name for calculated index raster.

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

    if mask_clouds:
        # Create masked AWEInsh
        # Mask bands before raster calculations
        blue_masked = cloud_mask(landsat_dir, blue_band)

        green_masked = cloud_mask(landsat_dir, green_band)
        nir_masked = cloud_mask(landsat_dir, nir_band)
        swir1_masked = cloud_mask(landsat_dir, swir1_band)
        swir2_masked = cloud_mask(landsat_dir, swir2_band)

        aweish_mask = ((blue_masked + 2.5 * green_masked - 1.5 *
                        (nir_masked + swir1_masked) - 0.25 * swir2_masked)
                       / (blue_masked + green_masked + nir_masked +
                          swir1_masked + swir2_masked))

        save_raster(aweish_mask, aweish_out, gdal.GDT_Float32, snap)

        return aweish_mask, print('Finished')

    if not mask_clouds:
        # Create unmasked AWEInsh
        # Perform Calculation
        aweish = ((blue_band + 2.5 * green_band - 1.5 * (nir_band + swir1_band)
                   - 0.25 * swir2_band)
                  / (blue_band + green_band + nir_band + swir1_band
                     + swir2_band))

        # Save Raster

        save_raster(aweish, aweish_out, gdal.GDT_Float32, snap)

        return aweish, print('Finished')


def AWEInsh(landsat_dir, aweinsh_out, mask_clouds=False):
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

            aweinsh_out :: str, required
                * Output path and file name for calculated index raster.

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

    if mask_clouds:
        # Create masked AWEInsh
        # Mask bands before raster calculations
        green_masked = cloud_mask(landsat_dir, green_band)
        nir_masked = cloud_mask(landsat_dir, nir_band)
        swir1_masked = cloud_mask(landsat_dir, swir1_band)

        aweinsh_mask = ((4 * (green_masked - swir1_masked)
                         - (0.25 * nir_masked + 2.75 * swir1_masked)) /
                        (green_masked + swir1_masked + nir_masked))

        save_raster(aweinsh_mask, aweinsh_out, gdal.GDT_Float32, snap)

        return aweinsh_mask, print('Finished')

    if not mask_clouds:
        # Create unmasked AWEInsh
        aweinsh = ((4 * (green_band - swir1_band) -
                    (0.25 * nir_band + 2.75 * swir1_band)) /
                   (green_band + swir1_band + nir_band))

        save_raster(aweinsh, aweinsh_out, gdal.GDT_Float32, snap)

        return aweinsh, print('Finished')


def NDMI(landsat_dir, ndmi_out):
    """
    NDMI(landsat_dir, ndmi_out)

    Calculates the Normalized Difference Moisture Index with Landsat-8
    and outputs a TIFF raster file.

    NDMI = (NIR - SWIR1) / (NIR + SWIR1)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ndmi_out :: str, required
                * Output path and file name for calculated index raster.
    """
    # Create list with file names
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    swir1 = glob(os.path.join(landsat_dir, '/*B6*'))

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
    ndmi = ((nir_band - swir1_band) / (nir_band + swir1_band))

    # Save Raster

    save_raster(ndmi, ndmi_out, gdal.GDT_Float32, snap)

    return ndmi, print('Finished')


def MNDWI(landsat_dir, mndwi_out):
    """
    MNDWI(landsat_dir, mndwi_out)

    Calculates the Modified Normalized Difference Water Index with Landsat-8
    and outputs a TIFF raster file.

    MNDWI = (Green - SWIR1) / (Green + SWIR1)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            mndwi_out :: str, required
                * Output path and file name for calculated index raster.
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
    mndwi = ((green_band - swir1_band) / (green_band + swir1_band))

    # Save Raster
    save_raster(mndwi, mndwi_out, gdal.GDT_Float32, snap)

    return mndwi, print('Finished')


# Vegetation indices
def NDVI(landsat_dir, ndvi_out, mask_clouds=False):
    """
    NDVI(landsat_dir, ndvi_out, mask_clouds=False)

    Calculates the Normalized Difference Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    NDVI = ((NIR - Red) / (NIR + Red))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ndvi_out :: str, required
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

    if mask_clouds:
        nir_masked = cloud_mask(landsat_dir, nir_band)
        red_masked = cloud_mask(landsat_dir, red_band)

        ndvi_masked = ((nir_masked - red_masked) / (nir_masked + red_masked))

        save_raster(ndvi_masked, ndvi_out, gdal.GDT_Float32, snap)

    if not mask_clouds:
        # Perform Calculation
        ndvi = ((nir_band - red_band) / (nir_band + red_band))

        # Save Raster
        save_raster(ndvi, ndvi_out, gdal.GDT_Float32, snap)

    return


def GNDVI(landsat_dir, gndvi_out):
    """
    GNDVI(landsat_dir, gndvi_out)

    Calculates the Green Normalized Difference Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    GNDVI = (NIR - Green) / (NIR + Green)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            gndvi_out :: str, required
                * Output path and file name for calculated index raster.

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
    gndvi = ((nir_band - green_band) / (nir_band + green_band))

    # Save Raster
    save_raster(gndvi, gndvi_out, gdal.GDT_Float32, snap)

    return gndvi, print('Finished')


def SAVI(landsat_dir, savi_out, soil_brightness=0.5, ):
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

            savi_out :: str, required
                * Output path and file name for calculated index raster.

            soil_brightness :: float, required (default=0.5)
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
    savi = ((nir_band - red_band) / (nir_band + red_band + soil_brightness)) \
           * (1 + soil_brightness)

    # Save Raster
    save_raster(savi, savi_out, gdal.GDT_Float32, snap)

    return savi, print('Finished')


def ARVI(landsat_dir, arvi_out):
    """
    ARVI(landsat_dir, arvi_out)

    Calculates the Atmospherically Resistant Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    ARVI = (NIR - (2 * Red) + Blue) / (NIR + (2 * Red) + Blue)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            arvi_out :: str, required
                * Output path and file name for calculated index raster.
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
    arvi = ((nir_band - (2 * red_band) + blue_band) /
            (nir_band + (2 * red_band) + blue_band))

    # Save Raster
    save_raster(arvi, arvi_out, gdal.GDT_Float32, snap)

    return arvi, print('Finished')


def VARI(landsat_dir, vari_out):
    """
    VARI(landsat_dir, vari_out)

    Calculates the Visual Atmospherically Resistant Index with Landsat-8
    and outputs a TIFF raster file.

    VARI = ((Green - Red) / (Green + Red - Blue))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            vari_out :: str, required
                * Output path and file name for calculated index raster.
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

    vari = ((green_band - red_band) / (green_band + red_band - blue_band))

    save_raster(vari, vari_out, gdal.GDT_Float32, snap)

    return vari, print('Finished')


# Urban and Landscape indices
def NDBI(landsat_dir, ndbi_out):
    """
    NDBI(landsat_dir, ndbi_out)

    Calculates the Normalized Difference Built-up Index with Landsat-8
    and outputs a TIFF raster file.

    NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ndbi_out :: str, required
                * Output path and file name for calculated index raster.
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
    ndbi = ((swir1_band - nir_band) / (swir1_band + nir_band))

    # Save Raster
    save_raster(ndbi, ndbi_out, gdal.GDT_Float32, snap)

    return ndbi, print('Finished')


def NDBaI(landsat_dir, ndbai_out):
    """
    NDBaI(landsat_dir, ndbai_out)

    Calculates the Normalized Difference Bareness Index with Landsat-8
    and outputs a TIFF raster file.

    NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ndbai_out :: str, required
                * Output path and file name for calculated index raster.

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
    ndbai = ((swir1_band - tir_band) / (swir1_band + tir_band))

    # Save Raster
    save_raster(ndbai, ndbai_out, gdal.GDT_Float32, snap)

    return ndbai, print('NDBaI raster created')


def NBLI(landsat_dir, nbli_out):
    """
    NBLI(landsat_dir, nbli_out)

    Calculates the Normalized Difference Bareland Index with Landsat-8
    and outputs a TIFF raster file.

    NBLI = (Red - TIR) / (Red + TIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            nbli_out :: str, required
                * Output path and file name for calculated index raster.

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
    nbli = ((red_band - tir_band) / (red_band + tir_band))

    # Save Raster
    save_raster(nbli, nbli_out, gdal.GDT_Float32, snap)

    return nbli, print('NBLI raster created.')


def EBBI(landsat_dir, ebbi_out):
    """
    EBBI(landsat_dir, ebbi_out)

    Calculates the Enhanced Built-up and Bareness Index with Landsat-8
    and outputs a TIFF raster file.

    EBBI = (SWIR1 - NIR) / (10 * (sqrt(SWIR1 + tir)))

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ebbi_out :: str, required
                * Output path and file name for calculated index raster
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
    # Save Raster
    save_raster(ebbi_mask, ebbi_out, gdal.GDT_Float32, snap)

    return ebbi_mask, print('EBBI raster created.')


def UI(landsat_dir, ui_out):
    """
    UI(landsat_dir, ui_out)

    Calculates the Urban Index with Landsat-8 and outputs a TIFF raster file.

    UI = (SWIR2 - NIR) / (SWIR2 + NIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            ui_out :: str, required
                * Output path and file name for calculated index raster.
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
    ui = ((swir2_band - nir_band) / (swir2_band + nir_band))

    # Save Raster
    save_raster(ui, ui_out, gdal.GDT_Float32, snap)

    return ui, print('UI raster created.')


# Fire indices
def NBRI(landsat_dir, nbri_out):
    """
    NBRI(landsat_dir, nbri_out)

    Calculates the Normalized Burn Ratio Index with Landsat-8 and outputs a
    TIFF raster file.

    UI = (SWIR2 - NIR) / (SWIR2 + NIR)

    Parameters:

            landsat_dir :: str, required
                * Folder path where all landsat bands for the scene are
                  contained.

            nbri_out :: str, required
                * Output path and file name for calculated index raster.

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
    nbri = ((nir_band - swir2_band) / (nir_band + swir2_band))

    # Save Raster
    save_raster(nbri, nbri_out, gdal.GDT_Float32, snap)

    return nbri, print('NBRI raster created.')
