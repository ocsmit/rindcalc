import os
import numpy as np
from osgeo import gdal
from glob import glob


def load_ls(landsat_dir):
    blue = glob(os.path.join(landsat_dir, '*B2*'))
    green = glob(os.path.join(landsat_dir, '*B3*'))
    red = glob(os.path.join(landsat_dir, '*B4*'))
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    swir1 = glob(os.path.join(landsat_dir, '*B6*'))
    swir2 = glob(os.path.join(landsat_dir, '*B7*'))
    tir = glob(os.path.join(landsat_dir, '*B10*'))

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

    tir_path = gdal.Open(os.path.join(landsat_dir, tir[0]))
    tir_band = tir_path.GetRasterBand(1).ReadAsArray().astype(np.float32)

    snap = gdal.Open(os.path.join(landsat_dir, blue[0]))

    band_dict = {"blue": blue_band, "green": green_band, "red": red_band,
                 "nir": nir_band, "swir1": swir1_band, "swir2": swir2_band,
                 "tir": tir_band, "snap": snap}

    return band_dict