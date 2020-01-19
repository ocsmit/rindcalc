import os
from glob import glob
from osgeo import gdal
import numpy as np
from scipy import stats


# Generic function to get landsat bands
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
    snap = red_path

    return blue_band, green_band, red_band, nir_band, swir1_band, swir2_band, tir_band, snap


def save_raster(in_array, out, snap):
    """

    :param in_array:
    :param out:
    :param snap:
    :return:
    """

    driver = gdal.GetDriverByName('GTiff')
    metadata = driver.GetMetadata()
    shape = in_array.shape
    dst_ds = driver.Create(out,
                           xsize=shape[1],
                           ysize=shape[0],
                           bands=1,
                           eType=gdal.GDT_Float32)
    proj = snap.GetProjection()
    geo = snap.GetGeoTransform()
    dst_ds.SetGeoTransform(geo)
    dst_ds.SetProjection(proj)
    dst_ds.GetRasterBand(1).WriteArray(in_array)
    dst_ds.FlushCache()
    dst_ds = None

    return in_array


def gen_stats(input_arr):
    min = np.nanmin(input_arr)
    max = np.nanmax(input_arr)

    std = np.nanstd(input_arr)
    return statistics
