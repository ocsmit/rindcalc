from osgeo import gdal
import numpy as np


def load_naip(in_naip):

    naip = gdal.Open(in_naip)
    red_band = naip.GetRasterBand(1).ReadAsArray().astype(np.float32)
    green_band = naip.GetRasterBand(2).ReadAsArray().astype(np.float32)
    blue_band = naip.GetRasterBand(3).ReadAsArray().astype(np.float32)
    nir_band = naip.GetRasterBand(4).ReadAsArray().astype(np.float32)
    snap = naip

    band_dict = {"blue": blue_band, "green": green_band, "red": red_band,
                 "nir": nir_band, "snap": snap}

    return band_dict
