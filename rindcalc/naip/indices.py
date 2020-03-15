import os
from osgeo import gdal
import numpy as np
from .bands_utils import save_raster, norm


def ARVI(in_naip, arvi_out):
    """
    ARVI(in_naip, arvi_out)

    Calculates the Atmospherically Resistant Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    ARVI = (NIR - (2 * Red) + Blue) / (NIR + (2 * Red) + Blue)

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

            arvi_out :: str, required
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
    arvi = ((nir_band - (2 * red_band) + blue_band) /
            (nir_band + (2 * red_band) + blue_band))
    # Save Raster
    save_raster(arvi, arvi_out, gdal.GDT_Float32, snap)
    print(arvi_out)


def VARI(in_naip, vari_out):
    """
     VARI(landsat_dir, vari_out)

    Calculates the Visual Atmospherically Resistant Index with NAIP imagery
    and outputs a TIFF raster file.

    VARI = ((Green - Red) / (Green + Red - Blue))

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

            vari_out :: str, required
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
    vari = ((2 * green_band - (red_band + blue_band)) /
            (2 * green_band + (red_band + blue_band)))
    # Save Raster
    save_raster(vari, vari_out, gdal.GDT_Float32, snap)

    print(vari_out)


def nVARI(in_naip, nvari_out):
    """
    nVARI(landsat_dir, vari_out)

     **Normalized between -1 - 1**

    Calculates the Visual Atmospherically Resistant Index with NAIP imagery
    and outputs a TIFF raster file.

    VARI = ((Green - Red) / (Green + Red - Blue))

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

            nvari_out :: str, required
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
    vari = ((2 * green_band - (red_band + blue_band)) /
            (2 * green_band + (red_band + blue_band)))
    normalized_vari = norm(vari, 1, 1)
    # Save Raster
    save_raster(normalized_vari, nvari_out, gdal.GDT_Float32, snap)

    print(nvari_out)


def NDVI(in_naip, ndvi_out):
    """
    NDVI(landsat_dir, ndvi_out, mask_clouds=False)

    Calculates the Normalized Difference Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    NDVI = ((NIR - Red) / (NIR + Red))

    Parameters:

            in_naip :: str, required
                * File path for NAIP image.

            ndvi_out :: str, required
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
    ndvi = ((nir_band - red_band) /
            (nir_band + red_band))
    # Save Raster
    save_raster(ndvi, ndvi_out, gdal.GDT_Float32, snap)

    print(ndvi_out)


def SAVI(in_naip, savi_out, soil_brightness=0.5):
    """
    SAVI(landsat_dir, soil_brightness=0.5, savi_out)

    Calculates the Soil Adjusted Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
                                        *L = Soil BrightnessFactor*

    Parameters:

            in_naip :: str, required
                *File path for NAIP image.

            savi_out :: str, required
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
    savi = (((nir_band - red_band) / (nir_band + red_band + soil_brightness))
            * (1 + soil_brightness))
    # Save Raster
    save_raster(savi, savi_out, gdal.GDT_Float32, snap)

    print(savi_out)
