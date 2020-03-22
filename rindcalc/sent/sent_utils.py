import os
import numpy as np
from osgeo import gdal
from glob import glob


# Todo: simplify get_bands
def get_bands(path):

    for dir, sub, files in os.walk(path):
        for f in files:
            ends = ['B01.jp2', 'B02.jp2', 'B03.jp2', 'B04.jp2', 'B05.jp2',
                    'B06.jp2', 'B07.jp2', 'B08.jp2', 'B8A.jp2', 'B09.jp2',
                    'B10.jp2', 'B11.jp2']
            if f.endswith(ends[0]):
                band_1 = os.path.join(dir, f)
            if f.endswith(ends[1]):
                band_2 = os.path.join(dir, f)
            if f.endswith(ends[2]):
                band_3 = os.path.join(dir, f)
            if f.endswith(ends[3]):
                band_4 = os.path.join(dir, f)
            if f.endswith(ends[4]):
                band_5 = os.path.join(dir, f)
            if f.endswith(ends[5]):
                band_6 = os.path.join(dir, f)
            if f.endswith(ends[6]):
                band_7 = os.path.join(dir, f)
            if f.endswith(ends[7]):
                band_8 = os.path.join(dir, f)
            if f.endswith(ends[8]):
                band_8A = os.path.join(dir, f)
            if f.endswith(ends[9]):
                band_9 = os.path.join(dir, f)
            if f.endswith(ends[10]):
                band_10 = os.path.join(dir, f)
            if f.endswith(ends[11]):
                band_11 = os.path.join(dir, f)

    return band_1, band_2, band_3, band_4, band_5, band_6, band_7, band_8, \
        band_8A, band_9, band_10, band_11
