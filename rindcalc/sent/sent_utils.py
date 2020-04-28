# ------------------------------------------------------------------------------
# Name: rindcalc.sent.sent_utils.py
# Author: Owen Smith, University of North Georgia IESA
# ------------------------------------------------------------------------------

import os


def get_bands(path):
    ends = ['B01.jp2', 'B02.jp2', 'B03.jp2', 'B04.jp2', 'B05.jp2',
            'B06.jp2', 'B07.jp2', 'B08.jp2', 'B8A.jp2', 'B09.jp2',
            'B10.jp2', 'B11.jp2']
    bands = []
    for i in range(len(ends)):
        for dir, sub, files in os.walk(path):
            for f in files:
                if f.endswith(ends[i]):
                    bands.append(os.path.join(dir, f))
    return bands
