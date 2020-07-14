import os
import numpy as np
from osgeo import gdal
from glob import glob


def load_ls(landsat_dir, dType=np.float32):
    ca = glob(os.path.join(landsat_dir,  '*B1*'))
    blue = glob(os.path.join(landsat_dir, '*B2*'))
    green = glob(os.path.join(landsat_dir, '*B3*'))
    red = glob(os.path.join(landsat_dir, '*B4*'))
    nir = glob(os.path.join(landsat_dir, '*B5*'))
    swir1 = glob(os.path.join(landsat_dir, '*B6*'))
    swir2 = glob(os.path.join(landsat_dir, '*B7*'))
    pan = glob(os.path.join(landsat_dir, '*B8*'))
    tir1 = glob(os.path.join(landsat_dir, '*B9*'))
    tir2 = glob(os.path.join(landsat_dir, '*B10*'))

    coastal_path = gdal.Open(os.path.join(landsat_dir, ca[0]))
    band_1 = coastal_path.GetRasterBand(1).ReadAsArray().astype(dType)

    blue_path = gdal.Open(os.path.join(landsat_dir, blue[0]))
    band_2 = blue_path.GetRasterBand(1).ReadAsArray().astype(dType)

    green_path = gdal.Open(os.path.join(landsat_dir, green[0]))
    band_3 = green_path.GetRasterBand(1).ReadAsArray().astype(dType)

    red_path = gdal.Open(os.path.join(landsat_dir, red[0]))
    band_4 = red_path.GetRasterBand(1).ReadAsArray().astype(dType)

    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    band_5 = NIR_path.GetRasterBand(1).ReadAsArray().astype(dType)

    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    band_6 = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(dType)

    SWIR2_path = gdal.Open(os.path.join(landsat_dir, swir2[0]))
    band_7 = SWIR2_path.GetRasterBand(1).ReadAsArray().astype(dType)

    pan_path = gdal.Open(os.path.join(landsat_dir, pan[0]))
    band_8 = pan_path.GetRasterBand(1).ReadAsArray().astype(dType)

    tir1_path = gdal.Open(os.path.join(landsat_dir, tir1[0]))
    band_9 = tir1_path.GetRasterBand(1).ReadAsArray().astype(dType)

    tir_path = gdal.Open(os.path.join(landsat_dir, tir2[0]))
    band_10 = tir_path.GetRasterBand(1).ReadAsArray().astype(dType)

    snap = gdal.Open(os.path.join(landsat_dir, blue[0]))

    band_dict = {"band_1": band_1, "band_2": band_2, "band_3": band_3,
                 "band_4": band_4, "band_5": band_5, "band_6": band_6,
                 "band_7": band_7, "band_8": band_8,  "band_9": band_9,
                 "band_10": band_10, "snap": snap}

    return band_dict

