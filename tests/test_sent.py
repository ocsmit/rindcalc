from rindcalc import Sentinel
import pytest
import sys
import numpy as np
sys.path.append('../rindcalc')

path = './tests/data/sent'
def test_sent_path():

    data = Sentinel(path)
    d = {'band_1': './tests/data/sent/B01.jp2', 
         'band_2': './tests/data/sent/B02.jp2', 
         'band_3': './tests/data/sent/B03.jp2',
         'band_4': './tests/data/sent/B04.jp2', 
         'band_5': './tests/data/sent/B05.jp2', 
         'band_6': './tests/data/sent/B06.jp2', 
         'band_7': './tests/data/sent/B07.jp2', 
         'band_8': './tests/data/sent/B08.jp2', 
         'band_8a': './tests/data/sent/B8A.jp2', 
         'band_9': './tests/data/sent/B09.jp2', 
         'band_10': './tests/data/sent/B10.jp2', 
         'band_11': './tests/data/sent/B11.jp2', 
         'band_12': './tests/data/sent/B12.jp2'}
    assert data.path == d


def test_sent_bands():
    data = Sentinel(path)
    bands = data.load_bands()
    d = {'band_1': [[1., 1., 0., 0., 0.],
                    [0., 1., 0., 1., 0.],
                    [0., 1., 0., 0., 1.],
                    [0., 0., 0., 0., 1.],
                    [0., 1., 1., 1., 0.]],
         'band_2': [[1., 1., 0., 1., 0.],
                    [0., 1., 0., 0., 1.],
                    [0., 0., 0., 1., 1.],
                    [0., 0., 0., 0., 0.],
                    [0., 1., 0., 0., 1.]],
         'band_3': [[0., 1., 0., 1., 1.],
                    [1., 1., 0., 0., 0.],
                    [1., 0., 1., 1., 1.],
                    [1., 1., 1., 0., 1.],
                    [0., 0., 1., 1., 1.]],
         'band_4': [[1., 1., 0., 0., 0.],
                    [0., 0., 0., 1., 0.],
                    [0., 1., 1., 1., 0.],
                    [0., 0., 1., 1., 1.],
                    [1., 1., 0., 0., 0.]],
         'band_5': [[1., 0., 1., 1., 0.],
                    [1., 0., 1., 0., 0.],
                    [1., 0., 0., 1., 0.],
                    [0., 1., 1., 0., 0.],
                    [0., 0., 0., 0., 1.]],
         'band_6': [[0., 1., 0., 1., 0.],
                    [0., 1., 0., 1., 0.],
                    [1., 1., 0., 1., 1.],
                    [1., 0., 1., 1., 0.],
                    [1., 1., 0., 1., 0.]],
         'band_7': [[1., 0., 1., 1., 1.],
                    [0., 0., 1., 1., 0.],
                    [0., 1., 1., 1., 0.],
                    [1., 0., 0., 1., 1.],
                    [0., 1., 1., 0., 1.]],
         'band_8': [[1., 0., 0., 0., 1.],
                    [1., 1., 1., 1., 1.],
                    [0., 0., 1., 0., 0.],
                    [0., 0., 0., 1., 1.],
                    [1., 0., 1., 0., 1.]],
         'band_8a': [[0., 1., 1., 1., 1.],
                    [1., 1., 0., 0., 0.],
                    [0., 1., 0., 0., 0.],
                    [0., 1., 0., 0., 1.],
                    [0., 1., 0., 1., 1.]],
         'band_9': [[0., 1., 1., 1., 1.],
                    [1., 0., 0., 1., 1.],
                    [1., 0., 0., 0., 0.],
                    [1., 0., 0., 0., 1.],
                    [1., 1., 1., 0., 1.]],
         'band_10': [[0., 1., 1., 1., 1.],
                    [1., 0., 0., 1., 1.],
                    [1., 0., 0., 0., 0.],
                    [1., 0., 0., 0., 1.],
                    [1., 1., 1., 0., 1.]],
         'band_11': [[1., 1., 0., 1., 0.],
                    [0., 0., 1., 1., 1.],
                    [1., 0., 1., 1., 1.],
                    [1., 0., 1., 0., 1.],
                    [1., 0., 1., 1., 0.]],
         'band_12': [[1., 1., 0., 0., 1.],
                    [0., 1., 1., 1., 1.],
                    [1., 0., 0., 1., 1.],
                    [1., 0., 0., 0., 1.],
                    [1., 1., 0., 0., 0.]]}
    for i in range(len(data.band_options)):
        assert np.array_equal(bands[data.band_options[i]],
                              d[data.band_options[i]])

def test_out():
    data = Sentinel(path).NDVI('./tests/data/senttest.tif')