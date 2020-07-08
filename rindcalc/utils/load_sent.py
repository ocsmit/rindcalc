# ------------------------------------------------------------------------------
# Name: rindcalc.sent.load_sent.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------
import os
from osgeo import gdal
import numpy as np


def load_sent(path):
    ends = ['B01.jp2', 'B02.jp2', 'B03.jp2', 'B04.jp2', 'B05.jp2',
            'B06.jp2', 'B07.jp2', 'B08.jp2', 'B8A.jp2', 'B09.jp2',
            'B10.jp2', 'B11.jp2']

    paths = []
    for i in range(len(ends)):
        for dir, sub, files in os.walk(path):
            for f in files:
                if f.endswith(ends[i]):
                    paths.append(os.path.join(dir, f))

    one = gdal.Open(paths[0])
    band_1 = one.GetRasterBand(1).ReadAsArray().astype(np.float32)
    two = gdal.Open(paths[1])
    band_2 = two.GetRasterBand(1).ReadAsArray().astype(np.float32)
    three = gdal.Open(paths[2])
    band_3 = three.GetRasterBand(1).ReadAsArray().astype(np.float32)
    four = gdal.Open(paths[3])
    band_4 = four.GetRasterBand(1).ReadAsArray().astype(np.float32)
    five = gdal.Open(paths[4])
    band_5 = five.GetRasterBand(1).ReadAsArray().astype(np.float32)
    six = gdal.Open(paths[5])
    band_6 = six.GetRasterBand(1).ReadAsArray().astype(np.float32)
    seven = gdal.Open(paths[6])
    band_7 = seven.GetRasterBand(1).ReadAsArray().astype(np.float32)
    eight = gdal.Open(paths[7])
    band_8 = eight.GetRasterBand(1).ReadAsArray().astype(np.float32)
    eight_a = gdal.Open(paths[8])
    band_8a = eight_a.GetRasterBand(1).ReadAsArray().astype(np.float32)
    nine = gdal.Open(path[9])
    band_9 = nine.GetRasterBand(1).ReadAsArray().astype(np.float32)
    ten = gdal.Open(paths[10])
    band_10 = ten.GetRasterBand(1).ReadAsArray().astype(np.float32)
    eleven = gdal.Open(paths[11])
    band_11 = eleven.GetRasterBand(1).ReadAsArray().astype(np.float32)
    twelve = gdal.Open(paths[12])
    band_12 = twelve.GetRasterBand(1).ReadAsArray().astype(np.float32)

    snap = gdal.Open(paths[1])

    bands = {"band_1": band_1, "band_2": band_2, "band_3": band_3,
             "band_4": band_4, "band_5": band_5, "band_6": band_6,
             "band_7": band_7, "band_8": band_8, "band_8a": band_8a,
             "band_9": band_9, "band_10": band_10, "band_11": band_11,
             "band_12": band_12, "snap": snap}

    return bands
