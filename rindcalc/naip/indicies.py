import os
from osgeo import gdal
import numpy as np
from .bands_utils import save_raster, norm


def ARVI(in_naip, out_raster):
    """
    Args:
        in_naip :: str : input naip tile
        out_raster :: str : output calculated raster
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
    arvi = ((nir_band - (2 * red_band) + blue_band) /
            (nir_band + (2 * red_band) + blue_band))
    # Save Raster
    save_raster(arvi, out_raster, gdal.GDT_Float32, snap)
    print(out_raster)


def VARI(in_naip, out_raster):
    """
    Args:
        in_naip :: str : input naip tile
        out_raster :: str : output calculated raster
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
    vari = ((2 * green_band - (red_band + blue_band)) /
            (2 * green_band + (red_band + blue_band)))
    # Save Raster
    save_raster(vari, out_raster, gdal.GDT_Float32, snap)

    print(out_raster)


def nVARI(in_naip, out_raster):
    """
    Args:
        in_naip :: str : input naip tile
        out_raster :: str : output calculated raster
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
    vari = ((2 * green_band - (red_band + blue_band)) /
            (2 * green_band + (red_band + blue_band)))
    normalized_vari = norm(vari, 1, 1)
    # Save Raster
    save_raster(normalized_vari, out_raster, gdal.GDT_Float32, snap)

    print(out_raster)
