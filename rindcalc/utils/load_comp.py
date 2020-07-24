# ------------------------------------------------------------------------------
# Name: rindcalc.sent.load_sent.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------
import os
from osgeo import gdal
import numpy as np
from glob import glob


def load_comp(path, which_bands):
    ends = ['*B01.jp2', '*B02.jp2', '*B03.jp2', '*B04.jp2', '*B05.jp2',
            '*B06.jp2', '*B07.jp2', '*B08.jp2', '*B8A.jp2', '*B09.jp2',
            '*B10.jp2', '*B11.jp2', '*B12.jp2']

    paths = []
    for i in range(len(ends)):
        paths.append(glob(os.path.join(path, ends[i])))
        #print(paths[i])

    bands = []

    for i in range(len(which_bands)):
        if which_bands[i] == 'band_1':
            bands.append(paths[0][0])

        if which_bands[i] == 'band_2':
            bands.append(paths[1][0])

        if which_bands[i] == 'band_3':
            bands.append(paths[2][0])

        if which_bands[i] == 'band_4':
            bands.append(paths[3][0])

        if which_bands[i] == 'band_5':
            bands.append(paths[4][0])

        if which_bands[i] == 'band_6':
            bands.append(paths[5][0])

        if which_bands[i] == 'band_7':
            bands.append(paths[6][0])

        if which_bands[i] == 'band_8':
            bands.append(paths[7][0])

        if which_bands[i] == 'band_8a':
            bands.append(paths[8][0])

        if which_bands[i] == 'band_9':
            bands.append(paths[9][0])

        if which_bands[i] == 'band_10':
            bands.append(paths[10][0])

        if which_bands[i] == 'band_11':
            bands.append(paths[11][0])

        if which_bands[i] == 'band_12':
            bands.append(paths[12][0])

    vrt = gdal.BuildVRT('tmp.vrt', bands, separate=True, bandList=[1,1,1])


    return vrt
