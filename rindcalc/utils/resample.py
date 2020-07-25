import numpy as np
from osgeo import gdal


def resample(band, cell_size, out=None):

    vrt = gdal.Translate('/vsimem/mem.vrt', band, xRes=cell_size, yRes=cell_size,
                         format='VRT')
    ds = gdal.Open('/vsimem/mem.vrt')
    array = ds.ReadAsArray().astype(np.float32)

    gdal.Unlink('/vsimem/mem.vrt')

    if out is not None:
        trans = gdal.Translate(out, vrt, format='GTiff')

    return array