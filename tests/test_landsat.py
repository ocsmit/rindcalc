from rindcalc import Landsat
import pytest
import sys
import numpy as np
sys.path.append('../rindcalc')
path = './tests/data/ls'


def test_ls_path():

    data = Landsat(path)
    d = {'band_1': './tests/data/ls/B1.TIF',
         'band_2': './tests/data/ls/B2.TIF',
         'band_3': './tests/data/ls/B3.TIF',
         'band_4': './tests/data/ls/B4.TIF',
         'band_5': './tests/data/ls/B5.TIF',
         'band_6': './tests/data/ls/B6.TIF',
         'band_7': './tests/data/ls/B7.TIF',
         'band_8': './tests/data/ls/B8.TIF',
         'band_9': './tests/data/ls/B9.TIF',
         'band_10': './tests/data/ls/B10.TIF',
         'band_qa': './tests/data/ls/BQA.TIF'}

    assert data.path == d


def test_ls_bands():

    data = Landsat(path)
    bands = data.load_bands()
    
    d = {'band_1': np.array([[0., 0., 1., 1., 1.],
                             [1., 1., 1., 0., 1.],
                             [0., 0., 0., 0., 0.],
                             [0., 0., 1., 1., 0.],
                             [0., 1., 1., 1., 1.]]),
         'band_2': np.array([[1., 1., 1., 1., 0.],
                             [0., 1., 1., 0., 0.],
                             [0., 0., 1., 0., 0.],
                             [0., 0., 1., 0., 0.],
                             [1., 0., 0., 1., 1.]]),
         'band_3': np.array([[1., 0., 0., 1., 0.],
                             [1., 1., 1., 0., 1.],
                             [0., 1., 0., 1., 0.],
                             [0., 1., 0., 1., 0.],
                             [1., 0., 1., 1., 1.]]),
         'band_4': np.array([[0., 0., 1., 1., 1.],
                             [0., 0., 0., 1., 0.],
                             [0., 1., 1., 0., 1.],
                             [1., 1., 0., 0., 0.],
                             [1., 0., 1., 0., 0.]]),
         'band_5': np.array([[1., 1., 0., 0., 0.],
                             [0., 0., 0., 0., 1.],
                             [1., 0., 1., 1., 0.],
                             [1., 1., 1., 0., 0.],
                             [1., 1., 1., 0., 0.]]),
         'band_6': np.array([[0., 0., 1., 0., 1.],
                             [1., 1., 1., 1., 1.],
                             [1., 0., 0., 1., 1.],
                             [0., 0., 0., 0., 0.],
                             [0., 1., 1., 0., 1.]]),
         'band_7': np.array([[1., 1., 1., 1., 1.],
                             [1., 0., 0., 0., 1.],
                             [1., 0., 1., 1., 0.],
                             [0., 1., 0., 1., 0.],
                             [1., 1., 0., 0., 1.]]),
         'band_8': np.array([[1., 1., 0., 0., 1.],
                             [0., 1., 1., 1., 1.],
                             [1., 0., 1., 1., 0.],
                             [1., 1., 1., 1., 0.],
                             [1., 0., 0., 0., 1.]]),
         'band_9': np.array([[1., 1., 1., 0., 1.],
                             [1., 0., 1., 1., 1.],
                             [1., 0., 1., 0., 1.],
                             [0., 1., 0., 1., 0.],
                             [1., 1., 1., 0., 0.]]),
         'band_10': np.array([[0., 1., 0., 1., 0.],
                              [0., 1., 0., 0., 1.],
                              [1., 0., 0., 0., 1.],
                              [0., 0., 0., 1., 1.],
                              [0., 0., 0., 0., 1.]]),
         'band_qa': np.array([[0., 1., 1., 0., 0.],
                              [1., 0., 1., 0., 1.],
                              [1., 1., 0., 1., 0.],
                              [1., 1., 0., 0., 0.],
                              [1., 0., 0., 0., 0.]])}

    for i in range(len(data.band_options)):
        print(bands[data.band_options[i]])
        print(np.array_equal(bands[data.band_options[i]],
                              d[data.band_options[i]]))

def test_out():
    data = Landsat(path).NDVI('./tests/data/lstest.tif')