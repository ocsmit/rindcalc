from rindcalc import NAIP
import pytest
import sys
import numpy as np

sys.path.append('../rindcalc')
path = './tests/data/naip.tif'


def test_naip_bands():
    data = NAIP(path)
    bands = data.load_bands()

    d = {'band_1': [[0., 1., 1., 1., 1.],
                    [0., 0., 1., 1., 0.],
                    [0., 0., 0., 0., 0.],
                    [1., 1., 1., 0., 1.],
                    [0., 0., 1., 1., 1.]],
         'band_2': [[1., 0., 0., 1., 1.],
                    [0., 0., 1., 0., 0.],
                    [0., 0., 1., 0., 0.],
                    [0., 1., 1., 0., 0.],
                    [1., 1., 1., 1., 0.]],
         'band_3': [[1., 0., 1., 1., 1.],
                    [0., 1., 0., 1., 0.],
                    [0., 1., 0., 1., 0.],
                    [1., 1., 1., 0., 1.],
                    [1., 0., 0., 1., 0.]],
         'band_4': [[1., 0., 1., 0., 0.],
                    [1., 1., 0., 0., 0.],
                    [0., 1., 1., 0., 1.],
                    [0., 0., 0., 1., 0.],
                    [0., 0., 1., 1., 1.]]}

    for i in range(len(data.band_options) - 1):
        assert np.array_equal(bands[data.band_options[i]],
                              d[data.band_options[i]])


def test_out():
    data = NAIP(path).NDVI('./tests/data/naiptest.tif')