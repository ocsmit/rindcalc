import pytest
import sys
sys.path.append('../rindcalc')
from rindcalc import Sentinel

def test_sent_path():
    path = './tests/data/sent'
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
    
