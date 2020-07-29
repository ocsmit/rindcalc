from rindcalc import Landsat
import pytest
import sys
import numpy as np
sys.path.append('../rindcalc')
path = './tests/data/ls'


def test_sent_path():

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


def test_sent_bands():

    data = Landsat(path)
    bands = data.load_bands()
    
    d = {'band_1': [[0., 0., 1., 1., 1.],
                    [1., 1., 1., 0., 1.],
                    [0., 0., 0., 0., 0.],
                    [0., 0., 1., 1., 0.],
                    [0., 1., 1., 1., 1.]],
         'band_2': [[1., 1., 1., 1., 0.],
                    [0., 1., 1., 0., 0.],
                    [0., 0., 1., 0., 0.],
                    [0., 0., 1., 0., 0.],
                    [1., 0., 0., 1., 1.]],
         'band_3': [[1., 0., 0., 1., 0.],
                    [1., 1., 1., 0., 1.],
                    [0., 1., 0., 1., 0.],
                    [0., 1., 0., 1., 0.],
                    [1., 0., 1., 1., 1.]],
         'band_4': [[0., 0., 1., 1., 1.],
                    [0., 0., 0., 1., 0.],
                    [0., 1., 1., 0., 1.],
                    [1., 1., 0., 0., 0.],
                    [1., 0., 1., 0., 0.]],
         'band_5': [[1., 1., 0., 0., 0.],
                    [0., 0., 0., 0., 1.],
                    [1., 0., 1., 1., 0.],
                    [1., 1., 1., 0., 0.],
                    [1., 1., 1., 0., 0.]],
         'band_6': [[0., 0., 1., 0., 1.],
                    [1., 1., 1., 1., 1.],
                    [1., 0., 0., 1., 1.],
                    [0., 0., 0., 0., 0.],
                    [0., 1., 1., 0., 1.]],
         'band_7': [[1., 1., 1., 1., 1.],
                    [1., 0., 0., 0., 1.],
                    [1., 0., 1., 1., 0.],
                    [0., 1., 0., 1., 0.],
                    [1., 1., 0., 0., 1.]],
         'band_8': [[1., 1., 0., 0., 1.],
                    [0., 1., 1., 1., 1.],
                    [1., 0., 1., 1., 0.],
                    [1., 1., 1., 1., 0.],
                    [1., 0., 0., 0., 1.]],
         'band_9': [[1., 1., 1., 0., 1.],
                    [1., 0., 1., 1., 1.],
                    [1., 0., 1., 0., 1.],
                    [0., 1., 0., 1., 0.],
                    [1., 1., 1., 0., 0.]],
         'band_10': [[0., 0., 0., 0., 1.],
                    [0., 0., 0., 1., 1.],
                    [1., 0., 0., 0., 1.],
                    [0., 1., 0., 0., 1.],
                    [0., 1., 0., 1., 0.]],
         'band_qa': [[1., 0., 0., 0., 0.],
                    [1., 1., 0., 0., 0.],
                    [1., 1., 0., 1., 0.],
                    [1., 0., 1., 0., 1.],
                    [0., 1., 1., 0., 0.]]}

    for i in range(len(data.band_options)):
        assert np.array_equal(bands[data.band_options[i]],
                              d[data.band_options[i]])
