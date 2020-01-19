import os
import numpy as np
from osgeo import gdal
from glob import glob


def cloud_mask(landsat_dir, band):
    """

    :param landsat_dir:
    :param band:
    :return:
    """

    # Get qa path
    qa = glob(landsat_dir + "/*BQA.tif")

    # Read band with gdal
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    qa_path = gdal.Open(os.path.join(landsat_dir, qa[0]))
    qa_band = qa_path.GetRasterBand(1).ReadAsArray().astype(np.uint32)

    # Change cloud values to 0 everything else to 1
    # Values from landsat 8 QA band
    mask_values = [2800, 2804, 2808, 2812, 6986, 6900, 6904, 6908,
                   2976, 2980, 2984, 2988, 3008, 3012, 3016, 3020,
                   7072, 7076, 7080, 7084, 7104, 7108, 7112, 7116]

    np.seterr(divide='ignore', invalid='ignore')


    m = np.ma.array(qa_band,
                    mask=np.logical_or.reduce([qa_band == value for value in mask_values]))
    np.ma.set_fill_value(m, 0)
    m1 = m.filled()
    m1[m1 != 0] = 1

    m1.reshape(qa_band.shape)

    mask = band * m1

    return mask

