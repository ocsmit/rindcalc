# ------------------------------------------------------------------------------
# Name: rindcalc.ls.cloud_masking.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import os
import numpy as np
from osgeo import gdal
from glob import glob


def cloud_mask_array(landsat_dir, array):
    """
    This function masks clouds in Landsat-8 imagery using the QA band and
    returns an array to save as a raster.
    """
    qa = glob(os.path.join(landsat_dir, '*BQA*'))
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    qa_path = gdal.Open(os.path.join(landsat_dir, qa[0]))
    qa_band = qa_path.GetRasterBand(1).ReadAsArray().astype(np.uint32)

    mask_values = [2800, 2804, 2808, 2812, 6986, 6900, 6904, 6908,
                   2976, 2980, 2984, 2988, 3008, 3012, 3016, 3020,
                   7072, 7076, 7080, 7084, 7104, 7108, 7112, 7116]
    np.seterr(divide='ignore', invalid='ignore')
    m = np.ma.array(qa_band,
                    mask=np.logical_or.reduce([qa_band == value
                                               for value in mask_values]))
    np.ma.set_fill_value(m, 0)
    m1 = m.filled()
    m1[m1 != 0] = 1

    m1.reshape(qa_band.shape)
    mask_array = array * m1
    mask_array[mask_array == 0] = np.nan

    return mask_array
