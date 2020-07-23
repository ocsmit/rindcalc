import os
from osgeo import gdal
import numpy as np


def save_comp(band1, band2, band3, out, snap, dType=gdal.GDT_Byte):

    if not os.path.exists(out):
        print('Writing raster')

    if os.path.exists(out):
        os.remove(out)
        print('Overwriting raster.')

    driver = gdal.GetDriverByName('GTiff')
    metadata = driver.GetMetadata()
    shape = band1.shape
    dst_ds = driver.Create(out,
                           xsize=shape[1],
                           ysize=shape[0],
                           bands=3,
                           eType=dType)
    proj = snap.GetProjection()
    geo = snap.GetGeoTransform()
    dst_ds.SetGeoTransform(geo)
    dst_ds.SetProjection(proj)
    dst_ds.GetRasterBand(1).WriteArray(band1)
    dst_ds.GetRasterBand(2).WriteArray(band2)
    dst_ds.GetRasterBand(3).WriteArray(band3)
    dst_ds.FlushCache()
    dst_ds = None
