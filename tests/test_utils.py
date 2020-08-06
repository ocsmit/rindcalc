from rindcalc.utils import save_index, resample
from rindcalc import Sentinel
import pytest
import sys
import numpy as np
sys.path.append('../rindcalc')
path = './tests/data/sent'

def test_save():
    data = Sentinel(path)
    bands = data.load_bands(['band_1'])

    save_index(bands['band_1'], './tests/data/save_index.tif', data.path['band_1'])

def test_resample():
    data = Sentinel(path)

    re_arr = resample(data.path['band_1'], 1, './tests/data/resample_test.tif')
