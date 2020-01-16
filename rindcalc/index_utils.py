"""
Functions for calculating spectral indexes of Landsat-8 bands
"""

import os
import numpy as np
from osgeo import gdal
from glob import glob


# Generic function to get band data. Not needed for using any other function
def GetBands(landsat_dir):
    """

    :param landsat_dir:
    :return:
    """
    # Create list with file names
    blue = glob(landsat_dir + "/*B2.tif")
    green = glob(landsat_dir + "/*B3.tif")
    red = glob(landsat_dir + "/*B4.tif")
    nir = glob(landsat_dir + "/*B5.tif")
    swir1 = glob(landsat_dir + "/*B6.tif")
    swir2 = glob(landsat_dir + "/*B7.tif")
    tir = glob(landsat_dir + "/*B10.tif")

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    blue_path = gdal.Open(os.path.join(landsat_dir, blue[0]))
    blue_band = blue_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    green_band = green_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    red_band = red_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR2_path = gdal.Open(os.path.join(landsat_dir, swir2[0]))
    swir2_band = SWIR2_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    TIR_path = gdal.Open(os.path.join(landsat_dir, tir[0]))
    tir_band = TIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)

    return blue_band, green_band, red_band, nir_band, swir1_band, swir2_band, tir_band


# Water Indices
def AWEIsh(landsat_dir, aweish_out):
    """

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

    # Perform Calculation
    aweish = ((blue_band + 2.5 * green_band - 1.5 * (nir_band + swir1_band) - 0.25 * swir2_band)
              / (blue_band + green_band + nir_band + swir1_band + swir2_band))

    # Save Raster
    if os.path.exists(aweish_out):
        raise IOError('AWEIsh raster already created')
    if not os.path.exists(aweish_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = aweish.shape
        dst_ds = driver.Create(aweish_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(aweish)
        dst_ds.FlushCache()
        dst_ds = None

    return aweish, print('AWEIsh raster created')


def AWEInsh(landsat_dir, aweinsh_out):
    """

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

    # Perform Calculation
    aweinsh = ((4 * (green_band - swir1_band) - (0.25 * nir_band + 2.75 * swir1_band)) /
               (green_band + swir1_band + nir_band))

    # Save Raster
    if os.path.exists(aweinsh_out):
        raise IOError('AWEInsh raster already created')
    if not os.path.exists(aweinsh_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = aweinsh.shape
        dst_ds = driver.Create(aweinsh_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(aweinsh)
        dst_ds.FlushCache()
        dst_ds = None

    return aweinsh, print('AWEInsh raster created')


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
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = ndmi.shape
        dst_ds = driver.Create(ndmi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(ndmi)
        dst_ds.FlushCache()
        dst_ds = None

    return ndmi, print('NDMI raster created.')


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
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = mndwi.shape
        dst_ds = driver.Create(mndwi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(mndwi)
        dst_ds.FlushCache()
        dst_ds = None

    return mndwi, print('MNDWI raster created.')


# Vegetation indices
def NDVI(landsat_dir, ndvi_out):
    """

    :param landsat_dir:
    :param ndvi_out:
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
    ndvi = ((nir_band - red_band) / (nir_band + red_band))

    # Save Raster
    if os.path.exists(ndvi_out):
        raise IOError('NDVI raster already created')
    if not os.path.exists(ndvi_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = ndvi.shape
        dst_ds = driver.Create(ndvi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(ndvi)
        dst_ds.FlushCache()
        dst_ds = None

    return ndvi, print('NDVI raster created.')


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
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = gndvi.shape
        dst_ds = driver.Create(gndvi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(gndvi)
        dst_ds.FlushCache()
        dst_ds = None

    return gndvi, print('Green NDVI raster created.')


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
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = savi.shape
        dst_ds = driver.Create(savi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(savi)
        dst_ds.FlushCache()
        dst_ds = None

    return savi, print('SAVI raster created.')


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
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = arvi.shape
        dst_ds = driver.Create(arvi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(arvi)
        dst_ds.FlushCache()
        dst_ds = None

    return arvi, print('ARVI raster created.')


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
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = ndbi.shape
        dst_ds = driver.Create(ndbi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(ndbi)
        dst_ds.FlushCache()
        dst_ds = None

    return ndbi, print('NDBI raster created.')


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
    snap = gdal.Open(os.path.join(landsat_dir, swir1[0]))

    # Perform Calculation
    ndbai = ((swir1_band - tir_band) / (swir1_band + tir_band))

    # Save Raster
    if os.path.exists(ndbai_out):
        raise IOError('NDBaI raster already created')
    if not os.path.exists(ndbai_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = ndbai.shape
        dst_ds = driver.Create(ndbai_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(ndbai)
        dst_ds.FlushCache()
        dst_ds = None

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
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = nbli.shape
        dst_ds = driver.Create(nbli_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(nbli)
        dst_ds.FlushCache()
        dst_ds = None

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
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = ebbi.shape
        dst_ds = driver.Create(ebbi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(ebbi_mask)
        dst_ds.FlushCache()
        dst_ds = None

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
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = ui.shape
        dst_ds = driver.Create(ui_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(ui)
        dst_ds.FlushCache()
        dst_ds = None

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
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = nbri.shape
        dst_ds = driver.Create(nbri_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(nbri)
        dst_ds.FlushCache()
        dst_ds = None

    return nbri, print('NBRI raster created.')
