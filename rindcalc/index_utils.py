"""
Functions for calculating spectral indexes of Landsat-8 bands
"""

import os
import numpy as np
from osgeo import gdal
from glob import glob
from .cloud_utils import cloud_mask
from .bands_utils import save_raster, gen_stats


# Water Indices
def AWEIsh(landsat_dir, aweish_out, mask_clouds):
    """

    :param mask_clouds:
    :param landsat_dir:
    :param aweish_out:
    :return:
    """
    # Create list with file names
    blue = glob(landsat_dir + "/*B2.tif")
    green = glob(landsat_dir + "/*B3.tif")
    nir = glob(landsat_dir + "/*B5.tif")
    swir1 = glob(landsat_dir + "/*B6.tif")
    swir2 = glob(landsat_dir + "/*B7.tif")

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

        aweish_mask = ((blue_masked + 2.5 * green_masked - 1.5 * (nir_masked + swir1_masked) - 0.25 * swir2_masked)
                       / (blue_masked + green_masked + nir_masked + swir1_masked + swir2_masked))
        if os.path.exists(aweish_out):
            raise IOError('Masked AWEIsh raster already created')
        if not os.path.exists(aweish_out):
            save_raster(aweish_mask, aweish_out, snap)
        return aweish_mask, print('Finished')

    if not mask_clouds:

        # Create unmasked AWEInsh
        # Perform Calculation
        aweish = ((blue_band + 2.5 * green_band - 1.5 * (nir_band + swir1_band) - 0.25 * swir2_band)
                  / (blue_band + green_band + nir_band + swir1_band + swir2_band))

        # Save Raster
        if os.path.exists(aweish_out):
            raise IOError('AWEIsh raster already created')
        if not os.path.exists(aweish_out):
            save_raster(aweish, aweish_out, snap)

        return aweish, print('Finished')


def AWEInsh(landsat_dir, aweinsh_out, mask_clouds):
    """

    :param mask_clouds:
    :param landsat_dir:
    :param aweinsh_out:
    :return:
    """
    # Create list with file names
    blue = glob(landsat_dir + "/*B2.tif")
    green = glob(landsat_dir + "/*B3.tif")
    nir = glob(landsat_dir + "/*B5.tif")
    swir1 = glob(landsat_dir + "/*B6.tif")
    swir2 = glob(landsat_dir + "/*B7.tif")

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

        aweinsh_mask = ((4 * (green_masked - swir1_masked) - (0.25 * nir_masked + 2.75 * swir1_masked)) /
                        (green_masked + swir1_masked + nir_masked))

        if os.path.exists(aweinsh_out):
            raise IOError('Masked NDVI raster already created')
        if not os.path.exists(aweinsh_out):
            save_raster(aweinsh_mask, aweinsh_out, snap)

        return aweinsh_mask, print('Finished')

    if not mask_clouds:

        # Create unmasked AWEInsh
        aweinsh = ((4 * (green_band - swir1_band) - (0.25 * nir_band + 2.75 * swir1_band)) /
                   (green_band + swir1_band + nir_band))

        if os.path.exists(aweinsh_out):
            raise IOError('Masked NDVI raster already created')
        if not os.path.exists(aweinsh_out):
            save_raster(aweinsh, aweinsh_out, snap)

        return aweinsh, print('Finished')


def NDMI(landsat_dir, ndmi_out):
    """

    :param landsat_dir:
    :param ndmi_out:
    :return:
    """
    # Create list with file names
    nir = glob(landsat_dir + "/*B5.tif")
    swir1 = glob(landsat_dir + "/*B6.tif")

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
    if os.path.exists(ndmi_out):
        raise IOError('NDMI raster already created')
    if not os.path.exists(ndmi_out):
        save_raster(ndmi, ndmi_out, snap)

    return ndmi, print('Finished')


def MNDWI(landsat_dir, mndwi_out):
    """

    :param landsat_dir:
    :param mndwi_out:
    :return:
    """
    # Create list with file names
    green = glob(landsat_dir + "/*B3.tif")
    swir1 = glob(landsat_dir + "/*B6.tif")

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
    if os.path.exists(mndwi_out):
        raise IOError('MNDWI raster already created')
    if not os.path.exists(mndwi_out):
        save_raster(mndwi, mndwi_out, snap)

    return mndwi, print('Finished')


# Vegetation indices
def NDVI(landsat_dir, ndvi_out, mask_clouds):
    """

    :param landsat_dir:
    :param ndvi_out:
    :param mask_clouds:
    :return:
    """
    # Create list with file names
    red = glob(landsat_dir + "/*B4.tif")
    nir = glob(landsat_dir + "/*B5.tif")

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

        if os.path.exists(ndvi_out):
            raise IOError('Masked NDVI raster already created')
        if not os.path.exists(ndvi_out):
            save_raster(ndvi_masked, ndvi_out, snap)

    if not mask_clouds:
        # Perform Calculation
        ndvi = ((nir_band - red_band) / (nir_band + red_band))

        # Save Raster
        if os.path.exists(ndvi_out):
            raise IOError('NDVI raster already created')
        if not os.path.exists(ndvi_out):
            save_raster(ndvi, ndvi_out, snap)

    return ndvi if mask_clouds is False else ndvi_masked


def GNDVI(landsat_dir, gndvi_out):
    """

    :param landsat_dir:
    :param gndvi_out:
    :return:
    """
    # Create list with file names
    green = glob(landsat_dir + "/*B3.tif")
    nir = glob(landsat_dir + "/*B5.tif")

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
    if os.path.exists(gndvi_out):
        raise IOError('Green NDVI raster already created')
    if not os.path.exists(gndvi_out):
        save_raster(gndvi, gndvi_out, snap)

    return gndvi, print('Finished')


def SAVI(landsat_dir, soil_brightness, savi_out):
    """

    :param landsat_dir:
    :param soil_brightness:
    :param savi_out:
    :return:
    """
    # Create list with file names
    red = glob(landsat_dir + "/*B4.tif")
    nir = glob(landsat_dir + "/*B5.tif")

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
    savi = ((nir_band - red_band) / (nir_band + red_band + soil_brightness)) * (1 + soil_brightness)

    # Save Raster
    if os.path.exists(savi_out):
        raise IOError('SAVI raster already created')
    if not os.path.exists(savi_out):
        save_raster(savi, savi_out, snap)

    return savi, print('Finished')


def ARVI(landsat_dir, arvi_out):
    # Create list with file names
    red = glob(landsat_dir + "/*B4.tif")
    nir = glob(landsat_dir + "/*B5.tif")
    blue = glob(landsat_dir + "/*B2.tif")

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
    arvi = ((nir_band - (2 * red_band) + blue_band) / (nir_band + (2 * red_band) + blue_band))

    # Save Raster
    if os.path.exists(arvi_out):
        raise IOError('ARVI raster already created')
    if not os.path.exists(arvi_out):
        save_raster(arvi, arvi_out, snap)

    return arvi, print('Finished')


# Urban and Landscape indices
def NDBI(landsat_dir, ndbi_out):
    """

    :param landsat_dir:
    :param ndbi_out:
    :return:
    """
    # Create list with file names
    nir = glob(landsat_dir + "/*B5.tif")
    swir1 = glob(landsat_dir + "/*B6.tif")

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
    if os.path.exists(ndbi_out):
        raise IOError('NDBI raster already created')
    if not os.path.exists(ndbi_out):
        save_raster(ndbi, ndbi_out, snap)

    return ndbi, print('Finished')


def NDBaI(landsat_dir, ndbai_out):
    """

    :param landsat_dir:
    :param ndbai_out:
    :return:
    """
    # Create list with file names
    swir1 = glob(landsat_dir + "/*B6.tif")
    tir = glob(landsat_dir + "/*B10.tif")

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
    if os.path.exists(ndbai_out):
        raise IOError('NDBaI raster already created')
    if not os.path.exists(ndbai_out):
        save_raster(ndbai, ndbai_out, snap)

    return ndbai, print('NDBaI raster created')


def NBLI(landsat_dir, nbli_out):
    """

    :param landsat_dir:
    :param nbli_out:
    :return:
    """
    # Create list with file names
    red = glob(landsat_dir + "/*B4.tif")
    tir = glob(landsat_dir + "/*B10.tif")

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
    if os.path.exists(nbli_out):
        raise IOError('NBLI raster already created')
    if not os.path.exists(nbli_out):
        save_raster(nbli, nbli_out, snap)

    return nbli, print('NBLI raster created.')


def EBBI(landsat_dir, ebbi_out):
    """

    :param landsat_dir:
    :param ebbi_out:
    :return:
    """
    # Create list with file names
    nir = glob(landsat_dir + "/*B5.tif")
    swir1 = glob(landsat_dir + "/*B6.tif")
    tir = glob(landsat_dir + "/*B10.tif")

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
    if os.path.exists(ebbi_out):
        raise IOError('EBBI raster already created')
    if not os.path.exists(ebbi_out):
        save_raster(ebbi_mask, ebbi_out, snap)

    return ebbi_mask, print('EBBI raster created.')


def UI(landsat_dir, ui_out):
    """

    :param landsat_dir:
    :param ui_out:
    :return:
    """
    # Create list with file names
    nir = glob(landsat_dir + "/*B5.tif")
    swir2 = glob(landsat_dir + "/*B7.tif")

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
    if os.path.exists(ui_out):
        raise IOError('UI raster already created')
    if not os.path.exists(ui_out):
        save_raster(ui, ui_out, snap)

    return ui, print('UI raster created.')


# Fire indices
def NBRI(landsat_dir, nbri_out):
    """

    :param landsat_dir:
    :param nbri_out:
    :return:
    """
    # Create list with file names
    nir = glob(landsat_dir + "/*B5.tif")
    swir2 = glob(landsat_dir + "/*B7.tif")

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
    if os.path.exists(nbri_out):
        raise IOError('NBRI raster already created')
    if not os.path.exists(nbri_out):
        save_raster(nbri, nbri_out, snap)

    return nbri, print('NBRI raster created.')
