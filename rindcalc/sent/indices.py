import os
import numpy as np
from osgeo import gdal
from glob import glob
from rindcalc.sent.sent_utils import get_bands
from rindcalc.band_utils import save_raster


def NDVI(sent_dir, out_raster):

    bands = get_bands(sent_dir)

    nir = gdal.Open(bands[7])
    nir_band = nir.GetRasterBand(1).ReadAsArray().astype(np.float32)
    red = gdal.Open(bands[3])
    red_band = red.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = nir

    equation = (nir_band - red_band) / (nir_band + red_band)

    save_raster(equation, out_raster, snap, gdal.GDT_Float32)
    return equation, print('Finished')
